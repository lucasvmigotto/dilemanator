# dilemanator

Inspired by "After Dinner Amusements: Which Would You Choose?: 50 Amusing Dilemmas".

## Pre-requisites

* [Docker CE](https://docs.docker.com/engine/install/)
* [DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
  * [Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
* [Dev Cotainers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Google AI Studio](https://aistudio.google.com/apikey)

## Development

### Setup environment

1. Clone the repository

    * _SSH_:

        ```bash
        git clone git@github.com:lucasvmigotto/dilemanator.git
        ```

    * _HTTPS_:

        ```bash
        git clone https://github.com/lucasvmigotto/dilemanator.git
        ```

2. Copy the file `.env.example` and rename it to `.env`

    > In order to make the application functional, you must inform values for `APP__MODEL_APIKEY` and `APP__DILEMAS_SAMPLES_URL`
    >
    > Customize, if needed, the additional  inner values

### Application start

* Run the following command:

    ```bash
    streamlit run src/main.py \
        --server.headless True \
        --browser.gatherUsageStats False \
        --server.address "$APP__HOST" \
        --server.port "$APP__PORT" # --server.runOnSave True
    ```

    > Uncomment `--server.runOnSave True` to enable _hot reload_

## Deployment

### Build Docker Image

* Run the following command to build the image

```bash
GCP_PROJECT_ID='<GCloud Project Id>'
GCP_REPOSITORY_NAME='<Artifact repository name>'
IMAGE_NAME='dilemanator'
CONTAINER_REPOSITORY="us-central1-docker.pkg.dev/${GCP_PROJECT_ID}/${GCP_REPOSITORY_NAME}"
TAG="$(git describe --tags --abbrev=0)"
CONTAINER_PUSH_NAME="${CONTAINER_REPOSITORY}/${IMAGE_NAME}:${TAG}"

docker build \
    --tag "${CONTAINER_PUSH_NAME}" \
    -f Dockerfile \
    --progress plain \
    --no-cache \
    .
```

#### Running a test container

* Create a container to test the builded image:

    ```bash
    docker run \
        --rm \
        --name "test_container" \
        --publish 8080:8080 \
        --env APP__DILEMAS_SAMPLES_URL="<Dilemas samples URL>" \
        --env APP__MODEL_APIKEY="<Gemini API Key>" \
        "${CONTAINER_PUSH_NAME}"
    ```

### Deploy

#### Google Cloud Platform (Cloud Run)

* Check the prerequisites:
  * [CLI initiation](https://cloud.google.com/sdk/docs/initializing)
  * [Docker authenticaation resolver](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images)

* Publish the builded image in Artifact Registry

    ```bash
    docker push "${CONTAINER_PUSH_NAME}"
    ```

## TODO

* Adjust workflow to use created dilemas history in prompt;
* Setup _CI/CD_ with [Google Cloud Artifact Registry](https://cloud.google.com/artifact-registry/docs) and [Google Cloud Cloud Run](https://cloud.google.com/run/docs/overview/what-is-cloud-run).


## References

* [LangChain - Google Genai](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)
* [LangGraph](https://langchain-ai.github.io/langgraph/)
* [Google AI](https://ai.google.dev/gemini-api/docs)
