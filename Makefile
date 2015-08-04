install-deps:
	pip install -r requirements.txt
	wget -P pytient/static/ -c http://code.jquery.com/jquery-2.1.4.min.js
	wget -P pytient/static/ -c http://code.jquery.com/ui/1.11.4/jquery-ui.min.js
