# CORS Proxy

In certain contexts, circumvention of CORS policies may be neccesssary for an application work correctly. One way of achieving this is through the use of a CORS proxy. This is essentially a web server which mirrors content from third-party origins such that they can be accessed without explicit CORS permissions. This repository contains a Python implementation which interprets the requested URL path as a *URL itself* and returns the resource found at that location.
