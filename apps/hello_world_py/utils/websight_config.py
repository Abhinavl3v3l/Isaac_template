def configure_websight_root(app):
    sight_component = app.nodes["websight"]["WebsightServer"]
    sight_component.config[
        "webroot"
    ] = "external/com_nvidia_isaac_sdk/packages/sight/webroot"
    sight_component.config["assetroot"] = "../isaac_assets"
