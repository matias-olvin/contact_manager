#!/bin/bash
echo "installing python-tk"

brew install python-tk

echo "Creating MongoDB Connection"

sudo mongod --dbpath /Users/olvin/Documents/contact_manager/data

echo "MongoDB connection closed"