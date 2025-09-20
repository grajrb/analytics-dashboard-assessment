import fs from 'fs'
import path from 'path'

export default function handler(req, res) {
  const { file } = req.query
  const allowed = [
    'growth_by_model_year',
    'top10_makes',
    'top10_models',
    'top10_cities',
    'top10_counties',
    'ev_type_distribution',
    'avg_range_by_model_year',
    'cafv_counts'
  ]
  if (!allowed.includes(file)) {
    res.status(404).end('Not found')
    return
  }
  const filePath = path.join(process.cwd(), 'outputs', `${file}.csv`)
  if (!fs.existsSync(filePath)) {
    res.status(404).end('Not found')
    return
  }
  const content = fs.readFileSync(filePath, 'utf8')
  res.setHeader('Content-Type', 'text/csv')
  res.status(200).send(content)
}
