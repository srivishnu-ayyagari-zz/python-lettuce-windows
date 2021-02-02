from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver

@before.all
def setup_browser():
    desired_capabilities = {
		"build" : "Python Lettuce",
		"name" : "Test1",
		"platform" : "Windows 10",
		"browserName" : "Chrome",
		"version" : "88.0"
	}

    world.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="https://srivishnua:lRPrFiIHat1GfMOOMISoBEcyPoa9XsABtLjAGw4flFgW2PjG1P@hub.lambdatest.com/wd/hub"
    )