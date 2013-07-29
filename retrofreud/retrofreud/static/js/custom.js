function vote(issue_id, inc) {
	$.get("/issues/vote/" + issue_id + "/", {'inc':inc}, function(){
		$('#issue_list').load('/issues/vote/');
	});
}

function sort_issues(path) {

	if($('#all_solved').closest('button').hasClass('active')) {
		path += '?solved=true';
	}
	$('#issue_list').load(path);
}

function vote_mood(profile_id, mood, inc) {

	$.get('/moodmeter/vote/' + profile_id + '/', {'mood' : mood,'inc':inc}, function() {
		$('#mood-meter').load( "/moodmeter/mood/" + profile_id + "/", function() {
			var new_data = [];
			new_data.push(parseInt($('#happy_score').text()));
			new_data.push(parseInt($('#excited_score').text()));
			new_data.push(parseInt($('#tired_score').text()));
			new_data.push(parseInt($('#sad_score').text()));
			new_data.push(parseInt($('#bored_score').text()));
			draw_mood_chart(new_data);
		});
	});
}

function add_thumb(profile_id, inc) {
	$.get('/moodmeter/vote/thumb/' + profile_id + '/', {'inc':inc}, function() {
		$("#thumbs-score").load( "/moodmeter/thumbs/" + profile_id + "/", function() {
			var downs = parseInt($('#thumbs_down').text());
			var ups = parseInt($('#thumbs_up').text());
			draw_thumbs_chart(ups,downs);
		});
	});
}


function draw_mood_chart(mood_data) {

		var data = {
			labels : ["Happy","Excited","Tired","Sad","Bored"],
			datasets : [
				{
					fillColor : "rgba(239,206,103,0.5)",
					strokeColor : "rgba(239,206,103,1)",
					pointColor : "rgba(239,206,103,1)",
					pointStrokeColor : "#601",
					data : mood_data
				}
			]
		}
		var options = {
			scaleOverride:true,scaleSteps:Math.max.apply(Math, mood_data),
			scaleStepWidth:1,scaleStartValue:0,
			pointLabelFontFamily : "'comfortaaregular'",
			scaleLineColor : "rgba(246,227,187,.5)"
		}
		var ctx = $("#mood_chart").get(0).getContext("2d");
		var myNewChart = new Chart(ctx).Radar(data, options);

	};

function draw_thumbs_chart(ups, downs) {

		var data = [{value: ups, color:"#5fbe5f"},
			{value : downs, color : "#faaa38"}]

		var options = {
			segmentStrokeColor : "#f6e3bb",
			segmentStrokeWidth : 1,
			percentageInnerCutout : 10
		}
		var ctx = $("#thumbs_chart").get(0).getContext("2d");
		var myNewChart = new Chart(ctx).Doughnut(data, options);
	};


function format_text(elem) {
	var txt = $(elem).html();

	if( txt.length > 0) {
		var str = $(elem).html().replace(/\n/g,"</li><li>")
		str = str.replace(/(<li><\/li>)+/g,"</ul><ul>");
		str = "<ul><li>" + str + "</li></ul>"
		$("#suggestions").html(str);
	} else {
		$("#suggestions").html('<span class="issue-default-text">Not defined yet.</span>')
	}
};


function updateSuggestions(id)
{
	$.post("/moodmeter/update/" + id + "/", $('#retro_suggestions').serialize(), function() {
		$("#suggestions").load( "/moodmeter/sug/" + id + "/", function() {
			format_text('#suggestions');
		});
	});
}

function update_issue_status(id)
{
	$('#issue-status').load('/issues/' + id + '/');
}

function close_issue(id, action) {
	if(action == 1) {
		$.get('/issues/close/' + id + '/', {}, function() {
			update_issue_status(id);
		});
	}
	else {
		$.get('/issues/open/' + id + '/', {}, function() {
			update_issue_status(id);
		});
	}
}

function updateActions(id)
{
	$.post("/issues/update/" + id + "/", $('#retro_actions').serialize(), function() {
		$("#suggestions").load( "/issues/actions/" + id + "/", function() {
			format_text('#suggestions');
		});
	});
}

