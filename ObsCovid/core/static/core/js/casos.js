$.getJSON(
	`https://coronavirus-19-api.herokuapp.com/countries/bolivia`,
	function(data) {
		console.log(data);
		var fecha = new Date();
		const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
		$(".update").append('Ultima actualizacion: ' + fecha.toLocaleDateString(undefined, options));
		$(".cases").append(data.cases);
		$(".todaycases").append(data.todayCases);
		$(".recovered").append(data.recovered);
		$(".deaths").append(data.deaths);
		}
	);