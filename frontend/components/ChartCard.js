export default function ChartCard({ title, children, height = 420 }){
  return (
    <div className="bg-white rounded-lg shadow p-4 mx-auto" style={{width: '100%'}}>
      <div style={{width: '100%', height: height, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
        <div style={{width: '100%', height: '100%', maxWidth: 920, margin: '0 auto'}}>
          {/* Title moved into the inner content container so it aligns with chart area */}
          <h3 className="text-lg font-semibold mb-4 text-center">{title}</h3>
          {children}
        </div>
      </div>
    </div>
  )
}
