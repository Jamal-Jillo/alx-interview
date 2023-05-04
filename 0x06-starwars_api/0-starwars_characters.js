#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error: Could not retrieve movie information');
    process.exit(1);
  }

  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    request(characterUrl, function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.error('Error: Could not retrieve character information');
        return;
      }

      const character = JSON.parse(body).name;
      console.log(character);
    });
  }
});
