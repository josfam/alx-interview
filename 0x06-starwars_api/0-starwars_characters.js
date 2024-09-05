#!/usr/bin/node

const requestCallBack = require('request');
const util = require('util');
const request = util.promisify(requestCallBack);

let movieID = process.argv[2];
if (!movieID) {
  movieID = '';
} else {
  movieID = Number(movieID);
}
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const makeRequest = async function (url) {
  let details = '';
  try {
    const response = await request(url);
    if (response.statusCode !== 200) {
      console.log('This film does not exist');
      return;
    }
    details = JSON.parse(response.body);
  } catch {
    console.log('There was an error with this lookup');
    return;
  }
  return details;
};

const findCharacters = async function () {
  // fetch the data
  const details = await makeRequest(url);

  if (movieID === '') {
    const filmDetails = details.results;
    for (const filmDetail of filmDetails) {
      const characterLinks = filmDetail.characters;
      for (const characterLink of characterLinks) {
        const characterDetails = await makeRequest(characterLink);
        console.log(characterDetails.name);
      }
    }
  } else {
    const characterLinks = details.characters;
    for (const characterLink of characterLinks) {
      const characterDetails = await makeRequest(characterLink);
      console.log(characterDetails.name);
    }
  }
};

findCharacters();
