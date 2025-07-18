# Side By Side

## Getting Started

The following steps are required to run this project:

* Clone this repository
* Install `uv`[¹](#1-instructions-to-install-uv-can-be-found-in-their-documentation)
* Install Python 3.13 or newer[²](#2-instructions-to-install-python-via-uv-can-be-found-in-their-documentation)
* Install mandatory dependencies
  ```shell
  uv sync --no-dev
  ```

## Previews

In order to see a preview of the video, you need `ffplay`.
Unfortunately, this cannot be installed as a Python dependency. \
Instead, you have to download / install it separately[³](#2-instructions-to-install-python-via-uv-can-be-found-in-their-documentation),
and then add it to your `PATH` or place copy the file to the root of this repository.

## Development

Install development dependencies:

```shell
uv sync --dev
```

Upgrade and reinstall all dependencies:

```shell
uv sync --dev --upgrade
```

### pre-commit

Install pre-commit hook:

```shell
pre-commit install
```

Update pre-commit hooks:

```shell
pre-commit autoupdate
```

Run all checks:

```shell
pre-commit run -a
```

---

###### 1: Instructions to [install `uv`](https://docs.astral.sh/uv/getting-started/installation) can be found in their documentation.

###### 2: Instructions to [install Python via `uv`](https://docs.astral.sh/uv/guides/install-python) can be found in their documentation.

###### 3: Instructions to [download / install `ffplay`](https://ffmpeg.org/download.html) can be found in the `ffmpeg` documentation.
