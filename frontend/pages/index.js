import { useEffect, useState } from 'react'
import Papa from 'papaparse'
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell, Legend } from 'recharts'
import ChartCard from '../components/ChartCard'

const COLORS = ['#4f46e5', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']

function fetchCsv(name){
  return fetch(`/api/data/${name}`).then(r => r.text()).then(txt => Papa.parse(txt, { header: true }).data)
}

export default function Home(){
  const [growth, setGrowth] = useState([])
  const [makes, setMakes] = useState([])
  const [evTypes, setEvTypes] = useState([])

  useEffect(()=>{
    fetchCsv('growth_by_model_year').then(data=>{
      // data rows like: Model Year,count
      const parsed = data.map(r=>({ year: r[Object.keys(r)[0]], count: +r[Object.keys(r)[1]] })).filter(d=>d.year)
      setGrowth(parsed.sort((a,b)=>+a.year - +b.year))
    })
    fetchCsv('top10_makes').then(data=>{
      const parsed = data.map(r=>({ name: r[Object.keys(r)[0]], count: +r[Object.keys(r)[1]] }))
      setMakes(parsed)
    })
    fetchCsv('ev_type_distribution').then(data=>{
      const parsed = data.map(r=>({ name: r[Object.keys(r)[0]], value: +r[Object.keys(r)[1]] }))
      setEvTypes(parsed)
    })
  }, [])

  return (
    <main className="container py-8">
      <h1 className="text-3xl font-bold mb-6">EV Analytics Dashboard</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <ChartCard title="EV Count by Model Year">
          <ResponsiveContainer>
            <LineChart data={growth}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="count" stroke="#4f46e5" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </ChartCard>

        <ChartCard title="Top Makes">
          <ResponsiveContainer>
            <BarChart data={makes} layout="vertical">
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis type="number" />
              <YAxis dataKey="name" type="category" />
              <Tooltip />
              <Bar dataKey="count" fill="#06b6d4" />
            </BarChart>
          </ResponsiveContainer>
        </ChartCard>

        <ChartCard title="EV Type Distribution">
          <ResponsiveContainer>
            <PieChart>
              <Pie data={evTypes} dataKey="value" nameKey="name" outerRadius={80} label>
                {evTypes.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </ChartCard>

        <div className="bg-white rounded-lg shadow p-4">
          <h3 className="text-lg font-semibold mb-2">Notes</h3>
          <p className="text-sm text-gray-600">Data is read from the repository `outputs/` CSV summaries via a Next.js API route. To update charts, re-run `scripts/generate_insights.py` and refresh this page.</p>
        </div>
      </div>
    </main>
  )
}
