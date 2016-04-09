This is a simple website watcher app that texts you when the website changes.

How to use with docker:
1. Edit site-checker/config.json - use the example_config.json as a template
2. docker build -t watch-site .
3. docker run -d --rm  watch-site

How to use standalone:
1. Edit site-checker/config.json - use the example_config.json as a template
2. cd site-checker; nohup python monitor_site.py
3. press ctrl-z
4. exit


Additional details:

It only looks at html - doesn't take screenshots or evaluate js. 

It only does one website.

It sends texts with twilio - you need to have an account and number and token - the free trial should work.
