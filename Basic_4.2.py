<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>home</title>
</head>
<body>
	<h1>This is the Home Page.</h1>
		<div>
			{% for i in specs %}
			<p><h2>{{i.company}}</h2> Pesents, the Complete New <h2>{{i.model}}</h2>,
				in 3 variants , which include {{i.color}} and the price strikes : {{i.price}}.</p>
			{% if i.if_donate %}
				<h3><u>if you choose {{i.color}} item then 3 % of revenue will be donated to Orphanges , Schools, etc.</u></h3>
			{% else %}
				<h3><u>Sorry, actually this coloured phone i.e {{i.color}} revenue will not be donated at any case. </u></h3>
			{% endif %}
			{% endfor %}
		</div>
</body>
</html>
