# Browser specific methods
These methods are used to get user agents of a specific browser easily. Under the hood it calls [`get`](get.md) method with relavant enum for the browser.

## Arguments
All of thse methods accept following arguments,

- `as_gen` :bool (optional) - Return value as a generator rather than a list. Defaults to `False`

## Methods
- `chrome` - Returns the user agents of the google chrome browser
    - Example,
        ```python
        fa.chrome()
        ```
- `firefox` - Returns the user agents of the firefox browser
    - Example,
        ```python
        fa.firefox()
        ```
- `edge` - Returns the user agents of the edge browser
    - Example,
        ```python
        fa.edge()
        ```
- `opera` - Returns the user agents of the opera browser
    - Example,
        ```python
        fa.opera()
        ```
- `safari` - Returns the user agents of the safari browser
    - Example,
        ```python
        fa.safari()
        ```
- `internet_explorer` - Returns the user agents of the internet explorer browser
    - Example,
        ```python
        fa.internet_explorer()
        ```