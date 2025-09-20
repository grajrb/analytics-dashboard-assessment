import { useEffect, useState } from 'react'
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, PieChart, Pie, Cell, Legend } from 'recharts'
import ChartCard from '../components/ChartCard'
import EVGrowthChart from '../components/EVGrowthChart'
import TopMakesChart from '../components/TopMakesChart'
import TopModelsChart from '../components/TopModelsChart'

const COLORS = ['#4f46e5', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']

async function fetchJson(){
  const res = await fetch('/ev_data.json')
  if(!res.ok) return []
  return res.json()
}

export default function Home(){
  const [growth, setGrowth] = useState([])
  const [makes, setMakes] = useState([])
  const [evTypes, setEvTypes] = useState([])

  useEffect(()=>{
    fetchJson().then(all =>{
      if(!all || all.length===0) return
      // all is array of vehicle records. Compute summaries client-side.
      const byYear = {}
      const makeCounts = {}
      const evTypeCounts = {}
      all.forEach(r=>{
        const year = r['Model Year'] || r['Model_Year'] || r['model_year']
        const make = r['Make']
        const evtype = r['Electric Vehicle Type']
        if(year){ byYear[year] = (byYear[year]||0) + 1 }
        if(make){ makeCounts[make] = (makeCounts[make]||0) + 1 }
        if(evtype){ evTypeCounts[evtype] = (evTypeCounts[evtype]||0) + 1 }
      })
      const growthArr = Object.entries(byYear).map(([year,count])=>({ year, count })).sort((a,b)=>+a.year - +b.year)
      const makesArr = Object.entries(makeCounts).map(([name,count])=>({ name, count })).sort((a,b)=>b.count-a.count).slice(0,10)
      const evTypesArr = Object.entries(evTypeCounts).map(([name,value])=>({ name, value }))
      setGrowth(growthArr)
      setMakes(makesArr)
      setEvTypes(evTypesArr)
    })
  }, [])

  return (
    <main className="container py-8">
      <h1 className="text-3xl font-bold mb-6 text-center">EV Analytics Dashboard</h1>

  <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mx-auto" style={{maxWidth: 1200, margin: '0 auto', paddingRight: '6%'}}>
        <ChartCard title="EV Count by Model Year" height={520}>
          <EVGrowthChart data={growth} />
        </ChartCard>

        <ChartCard title="Top Makes" height={520}>
          <TopMakesChart data={makes} />
        </ChartCard>

        <ChartCard title="Top Models" height={520}>
          <TopModelsChart data={/* compute top models from JSON if needed */ makes} />
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
      </div>
    </main>
  )
}
