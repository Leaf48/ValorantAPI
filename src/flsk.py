from flask import render_template, request, jsonify, Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache
from src.val import getJson

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
limiter = Limiter(app, key_func=get_remote_address)
cache = Cache(app)

successRequests = 0
failedRequests = 0


@app.route("/", methods=["GET"])
@limiter.limit("10/minute")
@cache.cached(timeout=3600)
def index():
    try:
        exampleName = "SEN TenZ".lower()
        exampleTag = "0505".lower()
        r = getJson(exampleName, exampleTag, "profile")

        status = {
            "status": "success",
            "username": r["stats"]["standardProfiles"][f"valorant|riot|{exampleName}#{exampleTag}"]["platformInfo"]
        }

        return jsonify(status)

    except Exception as err:
        status = {
            "status": "failed"
        }

        return jsonify(status)


@app.route("/metrics", methods=["GET"])
@limiter.limit("10/minute")
@cache.cached(timeout=60)
def metrics():
    data = {
        "total": successRequests + failedRequests,
        "success": successRequests,
        "failed": failedRequests
    }

    return data


@app.route("/valorant", methods=["GET"])
@limiter.limit("60/minute")
@cache.cached(timeout=600, query_string=True)
def valorant():
    global successRequests, failedRequests
    if request.method == "GET":
        try:
            username = request.args.get("username").lower()
            userTag = request.args.get("tag").lower()
            requestType = request.args.get("type").lower()
            requestType = requestType if requestType == ("matches" or "profile") else "profile"

            successRequests += 1
            if requestType == "profile":
                r = getJson(username, userTag, requestType)

                statsJson = r["stats"]["standardProfiles"][f"valorant|riot|{username}#{userTag}"]

                status = {
                    "status": "success",
                    "username": statsJson["platformInfo"],
                    "stats": statsJson["segments"][0]
                }

                return jsonify(status)

            else:
                failedRequests += 1
                status = {
                    "status": "failed"
                }

                return jsonify(status)

        except Exception as err:
            print(err)
            failedRequests += 1
            status = {
                "status": "failed"
            }

            return jsonify(status)
