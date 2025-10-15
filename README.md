# Task 2 - GitHub Actions CI/CD (Sample Node.js app)

This repository contains a ready-to-run example for Task 2:

- Node.js sample app
- Dockerfile
- Kubernetes manifests (k8s/)
- GitHub Actions workflows (CI and CD)

## What the workflows do
- **CI** (`.github/workflows/ci.yml`): installs dependencies, runs tests, builds Docker image and pushes to GitHub Container Registry (GHCR).
- **CD** (`.github/workflows/cd.yml`): on push to `main`, deploys the image to a Kubernetes cluster using manifests in `k8s/`. It waits for rollout; if rollout fails it attempts `kubectl rollout undo`.

## Required repository secrets (GitHub)
- `REGISTRY_USERNAME` — registry username (for GHCR you can use your GitHub username or a PAT)
- `REGISTRY_TOKEN` — registry token/PAT with write:packages permission for GHCR (or Docker Hub token)
- `REGISTRY_OWNER` — owner/org for the registry (your GitHub username or org)
- `KUBE_CONFIG_DATA` — base64-encoded kubeconfig file with access to the target cluster

To create `KUBE_CONFIG_DATA`:
```
cat ~/.kube/config | base64 | tr -d '\n'
```

## Quick steps to run
1. Create a GitHub repo and push this code.
2. Add the required secrets in Settings -> Secrets -> Actions.
3. Push to `develop` or `main`: CI will run, build the image and push to GHCR.
4. Merge to `main`: CD will run and deploy to your cluster.

## Notes
- To use Docker Hub instead of GHCR, update `ci.yml` `registry` and `tags` accordingly.
- For EKS/GKE/AKS, consider using provider-specific GitHub Actions to authenticate instead of storing kubeconfig when feasible.
