#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  process.exit(1);
}

const movieId = process.argv[2];

function fetchCharacters(urlList, index) {
  if (index >= urlList.length) {
    process.exit(0);
  }

  request(urlList[index], (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.log(error);
      fetchCharacters(urlList, index + 1);
      return;
    }

    const character = JSON.parse(body);
    console.log(character.name);
    fetchCharacters(urlList, index + 1);
  });
}

request(`https://swapi.dev/api/films/${movieId}`, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.log(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  fetchCharacters(characters, 0);
});