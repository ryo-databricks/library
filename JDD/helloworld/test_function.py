# Databricks notebook source
def hello():
  print("Hello")

# COMMAND ----------

def world(x):
  if x is not None:
    y = "World" + x
  else:
    y = "Good Bye"
  return y
