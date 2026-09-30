# Log Output Application

A simple application built for the DevOps with Kubernetes course (Exercise 1.1).

## Overview

1. Generates a random string (UUID) on startup.
2. Every 5 seconds, outputs timestamp + UUID.

## Quick Start

```bash
docker build -t log-output .
kubectl apply -f manifests/deployment.yaml
```
