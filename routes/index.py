from cgitb import reset
from crypt import methods
from flask import Flask, request, flash, jsonify
import json
import requests
import os
from . import routes
from packages.CreateDockerFile import createDockerFile
from packages import PullBranch


@routes.route('/api/dockerbuild', methods=["POST"])
def createDockerBuild():
    if request.method == "POST":
        req = request.json
        login_verify = "http://localhost:5000/api/verify"
        headerget = {'Content-Type': 'application/json', 'token': req["token"]}
        response = requests.post(
            login_verify, headers=headerget).content.decode("utf8")
        if json.loads(response)["token"] == "success":
            return createDockerFile(github_repo=req["github_repo"], docker_image=req['docker_image'])
        else:
            return jsonify({"status": "access denied"})


@routes.route('/api/pullbranch', methods=["POST"])
def pullBranch():
    if request.method == "POST":
        req = request.json
        print(req)
        login_verify = "http://localhost:5000/api/verify"
        headerget = {'Content-Type': 'application/json', 'token': req["token"]}
        response = requests.post(login_verify, headers=headerget).content.decode("utf8")
        if json.loads(response)["token"] == "success":
            response = PullBranch.pullBranch(github_repo=req["github_repo"], branch=req["branch"])
            return jsonify(response)
        else:
            return jsonify({"status": "access denied"})


@routes.route('/api/listapp', methods=["POST"])
def listApps():
    if request.method == "POST":
        req = request.json
        login_verify = "http://localhost:5000/api/verify"
        headerget = {'Content-Type': 'application/json', 'token': req["token"]}
        response = requests.post(
            login_verify, headers=headerget).content.decode("utf8")
        if json.loads(response)["token"] == "success":
            return jsonify({'path':'docker_deploys','apps_list': os.listdir('docker_deploys')})
        else:
            return jsonify({"status": "access denied"})




@routes.route('/api/login', methods=["POST"])
def login():
    if request.method == "POST":
        login_api = "http://localhost:5000/api/signup"
        req = request.json
        login_status = requests.post(login_api, json=req)
        return jsonify(json.loads(login_status.content.decode("utf8")))
