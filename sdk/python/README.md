# Pulumi Flux Provider

The Pulumi Flux Provider lets you create [Flux](http://fluxcd.io/) manifests used to bootstrap a Flux installation on Kubernetes.
This provider does not apply them, it only creates the manifests.

## Installing

Installing plugin, replacing $TAG with the current release
```bash
pulumi plugin install resource flux $TAG --server https://github.com/scav/pulumi-flux/releases/download/$TAG/ 
```

### Go

```bash
go get github.com/scav/pulumi-flux/sdk 
```

### Node

```bash
npm install @scav/pulumi-flux
```