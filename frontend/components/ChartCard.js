export default function ChartCard({ title, children }){
  return (
    <div className="bg-white rounded-lg shadow p-4">
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <div style={{width: '100%', height: 300}}>
        {children}
      </div>
    </div>
  )
}
