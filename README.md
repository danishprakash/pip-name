<h1 align="center">pip-name</h1>
<p align="center">Check whether a package name is available on PyPi</p>
<p align="center">
<img src="https://i.imgur.com/vL6Ip18.gif" height="250">
</p>

## Install

```console
$ pip install pip-name
```

## Usage

```sh
$ pip-name <name>
```

#### Examples

```sh
$ pip-name flake8
flake8 is unavailable

$ pip-name blake201
blake201 is available

$ pip-name chromatic
chromatic is unavailable
```

## Why?
Let's see, It's a pain in the ass to finally upload that module you've been writing for a while only to realize that a package with that same name already exists up there. 

## Contributing
Do you want to make this better? Open an issue and/or a PR on Github. Thanks!

## License
MIT License

Copyright (c) 2018 [Danish Prakash](https://github.com/prakashdanish)
