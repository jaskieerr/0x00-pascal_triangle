#!/usr/bin/node
// Star Wars API with JS

const fetch = require('request');
const MOVIE_ID = process.argv[2];

const API_BASE_URL = 'https://swapi-api.hbtn.io/api/films';

function fetchData(url) {
  return new Promise(function (resolve, reject) {
    fetch(url, function (err, response, data) {
      if (!err && response.statusCode === 200) {
        resolve(JSON.parse(data));
      } else {
        reject(err);
      }
    });
  });
}

async function displayCharacters(movieId) {
  const movieData = await fetchData(`${API_BASE_URL}/${movieId}`);
  for (const characterUrl of movieData.characters) {
    const character = await fetchData(characterUrl);
    console.log(character.name);
  }
}

displayCharacters(MOVIE_ID);
