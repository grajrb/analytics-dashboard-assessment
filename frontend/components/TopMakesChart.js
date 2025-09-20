import { BarChart, Bar, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts'

const COLORS = ['#06b6d4']

export default function TopMakesChart({ data }){
  return (
    <ResponsiveContainer>
      {/* reduce left margin and slightly reduce YAxis width to move bars left */}
  <BarChart data={data} layout="vertical" margin={{left:0, right:20, top:5, bottom:5}}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis type="number" />
  <YAxis dataKey="name" type="category" width={120} />
        <Tooltip />
        <Bar dataKey="count" fill={COLORS[0]} />
      </BarChart>
    </ResponsiveContainer>
  )
}
