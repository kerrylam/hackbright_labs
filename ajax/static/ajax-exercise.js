"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(evt) {

    $.get('/fortune', (response) => {
      $('#fortune-text').html(response);
    })
};

$('#get-fortune-button').on('click', showFortune);


// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {
      "zipcode": $("#zipcode-field").val()
    };

    $.get(url, formData, (response) => {
      $('#weather-info').text(`${response.forecast}`);

    })
};


$("#weather-form").on('submit', showWeather);


// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    let url = "/order-melons.json";
    const formData = {
      "melon_type": $('#melon-type-field').val(),
      "qty": $('#qty-field').val()
    };

    $.post(url, formData, (response) => {
      $('#order-status').text(`${response.msg}`);
    })

    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


