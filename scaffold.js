const fs = require('fs');
const crossfilter = require('crossfilter2')


const filepath = './data/SRR17309643/SRR17309643.csv';
const rows = fs.readFileSync(filepath).toString().split('\n');
const headers = rows[0].split(',');
const read_data = crossfilter(
  rows.splice(1).map(row => {
    let result = {};
    row.split(',').forEach((raw_datum, index) => {
      const header = headers[index];
      const datum = (header != 'mate_cigar' && header != 'name') ? +raw_datum : raw_datum;
      result[header] = datum;
    });
    return result;
  })
);

const read_starts = read_data.dimension(read_datum => read_datum.read_start);
read_starts.filterRange([0, 60]);
console.log(read_starts.top(1))
console.log(read_starts.bottom(1))
