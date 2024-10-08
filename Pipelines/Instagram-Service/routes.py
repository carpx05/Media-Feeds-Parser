from flask import Blueprint, jsonify
from utils.logger import LogType, log
from service import InstagramService

TAG = "Instagram-Service/routes.py"

instagram_bp = Blueprint("instagram", __name__)


@instagram_bp.route("/instagram/all", methods=["GET"])
def get_all_instagram():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        InstagramService.perform_login(username, password)

        try:
            parsed_home_data = InstagramService.parse_home()
        except Exception as _:
            parsed_home_data = None
            log(TAG, LogType.ERROR, "Failed to parse home data")

        try:
            parsed_explore_data = InstagramService.parse_explore()
        except Exception as _:
            parsed_explore_data = None
            log(TAG, LogType.ERROR, "Failed to parse explore data")

        try:
            parsed_profile_data = InstagramService.parse_profile(username)
        except Exception as _:
            parsed_profile_data = None
            log(TAG, LogType.ERROR, "Failed to parse profile data")

        try:
            login_activity = InstagramService.parse_login_activity()
        except Exception as _:
            login_activity = None
            log(TAG, LogType.ERROR, "Failed to parse login activity")

        return (
            jsonify(
                {
                    "home": parsed_home_data,
                    "explore": parsed_explore_data,
                    "profile": parsed_profile_data,
                    "login_activity": login_activity,
                }
            ),
            200,
        )

    except Exception as _:
        return jsonify({"error": "Invalid credentials"}), 400


@instagram_bp.route("/instagram/home", methods=["GET"])
def get_home_instagram():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        InstagramService.perform_login(username, password)

        try:
            parsed_home_data = InstagramService.parse_home()
        except Exception as _:
            parsed_home_data = None
            log(TAG, LogType.ERROR, "Failed to parse home data")

        return jsonify({"home": parsed_home_data}), 200

    except Exception as _:
        return jsonify({"error": "Invalid credentials"}), 400


@instagram_bp.route("/instagram/explore", methods=["GET"])
def get_explore_instagram():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        InstagramService.perform_login(username, password)

        try:
            parsed_explore_data = InstagramService.parse_explore()
        except Exception as _:
            parsed_explore_data = None
            log(TAG, LogType.ERROR, "Failed to parse explore data")

        return jsonify({"explore": parsed_explore_data}), 200

    except Exception as _:
        return jsonify({"error": "Invalid credentials"}), 400


@instagram_bp.route("/instagram/profile", methods=["GET"])
def get_profile_instagram():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        InstagramService.perform_login(username, password)

        try:
            parsed_profile_data = InstagramService.parse_profile(username)
        except Exception as _:
            parsed_profile_data = None
            log(TAG, LogType.ERROR, "Failed to parse profile data")

        return jsonify({"profile": parsed_profile_data}), 200

    except Exception as _:
        return jsonify({"error": "Invalid credentials"}), 400


@instagram_bp.route("/instagram/login-activity", methods=["GET"])
def get_login_activity():
    try:
        username = request.args.get("username")
        password = request.args.get("password")
        InstagramService.perform_login(username, password)

        try:
            login_activity = InstagramService.parse_login_activity()
        except Exception as _:
            login_activity = None
            log(TAG, LogType.ERROR, "Failed to parse login activity")

        return jsonify({"login_activity": login_activity}), 200

    except Exception as _:
        return jsonify({"error": "Invalid credentials"}), 400
