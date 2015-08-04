$(document).ready ->
  $.getJSON '/paciente.json',
    (data) ->
      $('#s').autocomplete {lookup: json2array data.pacientes}

json2array = (data) ->
  values = []
  $.each(data, (key, val) -> values.push val)
  values
