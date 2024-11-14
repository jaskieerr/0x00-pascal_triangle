#!/usr/bin/node
// Using Star Wars API

const request = require('request');
const FILMID = process.argv[2];

// Request URL
const URL_BASE = 'https://swapi-api.hbtn.io/api/films';

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error || new Error(`Request failed with status ${res.statusCode}`));
      }
    });
  });
}

// baba amana:
async function main (filmID) {
  try {
    const res = await doRequest(`${URL_BASE}/${filmID}`);
    for (const e of res.characters) {
      const pj = await doRequest(e);
      console.log(pj.name);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main(FILMID);
