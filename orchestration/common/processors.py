import re

def setup(request):
	current_url = request.get_full_path()
	get_url = current_url.split('?')
	base_url = get_url[0]
	split_url = base_url.split('/')
	current_page = split_url[1]

	nav = [
	{
	'name': 'Home',
	'url': '/',
	},
	{
	'name': 'Launch',
	'url': '/launch/',
	},
	{
	'name': 'Deployments',
	'url': '/deployments/',
	},
	]

	if current_page:
		for page in nav:
			if re.search(current_page, page['url']):
				page['class'] = 'active'
	else:
		nav[0]['class'] = 'active'
	
	context = {}
	context['orchestration_nav'] = nav
	return context