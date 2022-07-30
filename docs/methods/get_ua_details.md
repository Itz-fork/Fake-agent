# Get user agent details
Get user agent details such as os type, name, etc.

## Arguments
- `ua` :str - User agent

## Example
- Get user agent details
    ```python
    from FakeAgent import Fake_Agent
    
    fa = Fake_Agent()
    print(fa.get_ua_details("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36"))
    ```