<div id="top"></div>

<!-- TOP -->

[![API](https://img.shields.io/website?down_color=red&down_message=Not%20Working&label=API&style=for-the-badge&up_message=Working&url=https%3A%2F%2Fvalorantapiunofficial.herokuapp.com%2F)](https://valorantapiunofficial.herokuapp.com/)
[![Metrics](https://img.shields.io/website?down_color=red&down_message=Not%20Working&label=Metrics&style=for-the-badge&up_message=Working&url=https%3A%2F%2Fvalorantapiunofficial.herokuapp.com%2Fmetrics)](https://valorantapiunofficial.herokuapp.com/metrics)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Leaf48/ValorantAPI">
    <img src="https://user-images.githubusercontent.com/58620209/175783389-2497ed06-957d-4cdd-9fe1-d43f534cdc19.png" alt="Logo" width="80" height="80">

  </a>

  <h3 align="center">ValorantAPI</h3>

  <p align="center">
    Easy to use.
    <br />
    <br />
    <a href="https://github.com/Leaf48/ValorantAPI/issues">Report Bug</a>
    ·
    <a href="https://github.com/Leaf48/ValorantAPI/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
  <img src="https://media1.tenor.com/images/0a87fbcdd08e1280c12e26ac2c3bb443/tenor.gif" alt="Logo">
  <h4>I made it so that everyone could use it.</h4>
</div>


### Built With

* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started
- [ ] Base Endpoint
```url
https://valorantapiunofficial.herokuapp.com/
```
* Returns example
```json
{
  "status": "success", 
  "username": {
    "additionalParameters": null, 
    "avatarUrl": "", 
    "platformSlug": "riot", 
    "platformUserHandle": "example#12345", 
    "platformUserId": "", 
    "platformUserIdentifier": "example#12345"
}
```
</br>

### Parameter
- [ ] Get Player's Status </br>
```url
https://valorantapiunofficial.herokuapp.com/valorant/
```

| Name | Type | Desc | Required |
| ------------- | ------------- | ------------- | ------------- |
| username  | string  | Username(Ex. Example)  | yes  |
| tag  | string  | User's tag(Ex. 1234)  | yes |
| type  | string  | *profile* | yes  |

* Limit

| Cache | Request Limit |
| ----- | ----- |
| 600 secs | 60 / minutes |

</br>

- [ ] Get Metrics(How many times has API been used.)
```url
https://valorantapiunofficial.herokuapp.com/metrics/
```
* Return
```json
{
  "failed": 1, 
  "success": 1, 
  "total": 2
}
```
* Limit

| Cache | Request Limit |
| ----- | ----- |
| 60 secs | 10 / minutes |

### Example
- [ ] Get Someone's Status </br>
```url
https://valorantapiunofficial.herokuapp.com/valorant?username=xxxxxxxx&tag=xxxxxx&type=profile
```
