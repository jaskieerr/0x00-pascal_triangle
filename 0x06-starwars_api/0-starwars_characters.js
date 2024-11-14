#!/usr/bin/node
// using star wars API

const request = require('request');
const Film_id = process.argv[2];


const URL = 'https://swapi-api.hbtn.io/api/films';

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}



async function main (filmID) {
  const res = await doRequest(`${URL}/${filmID}`);
  for (const e of res.characters) {
    const pj = await doRequest(e);
    console.log(pj.name);
  }
}

main(Film_id);
