# React + Apollo + GraphQL Demo

This repository contains code that was shown at the [TalkJS Singapore June Meetup](https://www.meetup.com/Singapore-JS/events/240521034/).

The slides can be found [here](https://speakerdeck.com/mbrochh/using-apollo-with-reactjs-and-graphql).

This repo contains a simple Django project with one app called `simple_app`
and one model (called `Message`). After you cloned this repo, please create
a virtualenv in Python and install Django:

```bash
cd ~/Projects/
git clone https://github.com/mbrochh/react-apollo-graphql-demo.git
cd react-apollo-graphql-demo/backend
mkvirtualenv react-apollo-graphql-demo
pip install -r requirements.txt
./manage.py runserver 0.0.0.0:8000
```

Once you have the local devserver running, you should be able to login at
`/admin/` with user `admin` and password `start1234` and you should be able to
access `/graphql/`.
