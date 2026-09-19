<!--
  README for github.com/arazvant
  Palette from theaimerge.com: cream #F8F6F2, charcoal #1C1B19, terracotta #D95319.
  assets/header.svg and assets/cta-banner.svg are hand-built — the header is an animated
  grid of squares, styled like a GitHub contribution graph, sweeping in left-to-right in
  brand colors. Self-hosted, no third-party generator. Bump the ?v= query after edits —
  raw.githubusercontent.com caches aggressively and won't otherwise pick up changes.
  assets/profile-photo.gif is the pixel-portrait GIF, resampled to 5fps.

  Page flow: Who am I -> What I do -> Why follow -> CTAs -> Connect -> (activity)
-->

<p align="center">
  <img src="./assets/header.svg?v=3" width="100%" alt="Alex Razvant" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=18&duration=3000&pause=1200&color=D95319&center=true&vCenter=true&width=700&lines=Building+Vision+AI+%26+VLM+systems+at+Axon;Writing+The+AI+Merge+%E2%80%94+production+AI%2C+not+demos;10%2C000%2B+engineers+%C2%B7+NVIDIA+partner" alt="typing" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/-Axon-1C1B19?style=flat-square" />
<img src="https://img.shields.io/badge/-The%20AI%20Merge-1C1B19?style=flat-square" />
<img src="https://img.shields.io/badge/-NVIDIA%20Partner-D95319?style=flat-square&logo=nvidia&logoColor=F8F6F2" />
</p>

<br/>

## Who am I
<table>
<tr>
<td><img src="./assets/profile-photo.gif" width="95" height="95" align="left" alt="" /></td>
<td>I'm Alex - a Senior Software Engineer who spent a decade in AI. I also create content through The AI Merge, sharing the lessons I've learned.</td>
</tr>
</table>

## What I do

Building and teaching production AI systems - through The AI Merge.

**At Axon**

- Built the OS-to-cloud stack for a fleet of thousands of edge devices (NVIDIA Jetson, Raspberry Pi, embedded Linux) — Wind River Linux images, RAUC for A/B OTA updates, and AWS IoT Core / Device Shadows for fleet configuration and telemetry.
- Shipped a fully on-edge DeepStream AI pipeline on Jetson — optimized models and an expert system, wired into the edge-AI service stack to stream results to the cloud. Also designed a dynamic tiered config system pushed to devices as heartbeats over IoT Device Shadows.
- Built AI pipelines analyzing video at scale — semantic video search, image captioning, video summarization, and synthetic data generation for training, served through Triton inference on edge devices and in Kubernetes.
- Helped build Search: ~25 microservices spanning multiple clouds, ingesting device data into a large-scale search and filtering layer that holds a low p99 under load.
- Built agentic systems for on-call and incident management — coding-agent workflows and agents that triage production traces.
- Pushes internally for better AI-assisted engineering: knowledge sharing, tutorials, and workshops on using AI well as an engineer.

<table width="100%">
<tr><td width="60%"><a href="https://github.com/the-ai-merge/multimodal-agents-course"><b>Kubrick</b></a> — open-source multimodal AI agent course, built with Miguel Otero Pedrido</td><td align="right"><img src="https://img.shields.io/github/stars/the-ai-merge/multimodal-agents-course?style=flat-square&color=1C1B19&labelColor=F8F6F2" /></td></tr>
<tr><td><b>MAVS</b> — edge multi-agent vision system for wildlife conservation: MLOps, MCP/A2A agents, edge inference</td><td align="right"><sub>Soon</sub></td></tr>
<tr><td><b>Forge</b> — a human-gated workflow for building software with AI agents: you approve, agents execute in scope</td><td align="right"><sub>Soon</sub></td></tr>
<tr><td><b>Patch</b> — a local voice companion / desk assistant running on an NVIDIA DGX Spark, with an iPhone as its mic, display, and approval surface</td><td align="right"><sub>Soon</sub></td></tr>
</table>

I like to think about Software and AI grouped in three ladders, which is the way I also teach it.

**Foundations**

<img src="https://skillicons.dev/icons?i=python,go,kotlin,cpp,rust,pytorch,tensorflow,scikitlearn&theme=light" alt="Python, Go, Kotlin, C++, Rust, PyTorch, TensorFlow, scikit-learn" />

**Systems**

<table>
<tr>
<td align="center"><img src="https://img.shields.io/badge/-CUDA-1C1B19?style=flat-square&logo=nvidia&logoColor=F8F6F2" alt="CUDA"/></td>
<td align="center"><img src="https://img.shields.io/badge/-LangChain-1C1B19?style=flat-square&logo=langchain&logoColor=F8F6F2" alt="LangChain"/></td>
<td align="center"><img src="https://img.shields.io/badge/-MCP-1C1B19?style=flat-square" alt="MCP"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Anthropic-1C1B19?style=flat-square&logo=anthropic&logoColor=F8F6F2" alt="Anthropic"/></td>
<td align="center"><img src="https://img.shields.io/badge/-OpenAI-1C1B19?style=flat-square&logo=openai&logoColor=F8F6F2" alt="OpenAI"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Groq-1C1B19?style=flat-square" alt="Groq"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Ollama-1C1B19?style=flat-square&logo=ollama&logoColor=F8F6F2" alt="Ollama"/></td>
<td align="center"><img src="https://img.shields.io/badge/-OpenCV-1C1B19?style=flat-square&logo=opencv&logoColor=F8F6F2" alt="OpenCV"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Qdrant-1C1B19?style=flat-square&logo=qdrant&logoColor=F8F6F2" alt="Qdrant"/></td>
<td align="center"><img src="https://img.shields.io/badge/-vLLM-1C1B19?style=flat-square&logo=vllm&logoColor=F8F6F2" alt="vLLM"/></td>
<td align="center"><img src="https://img.shields.io/badge/-TensorRT-1C1B19?style=flat-square&logo=nvidia&logoColor=F8F6F2" alt="TensorRT"/></td>
<td align="center"><img src="https://img.shields.io/badge/-NVIDIA%20Triton-1C1B19?style=flat-square&logo=nvidia&logoColor=F8F6F2" alt="NVIDIA Triton"/></td>
<td align="center"><img src="https://img.shields.io/badge/-NVIDIA%20DeepStream-1C1B19?style=flat-square&logo=nvidia&logoColor=F8F6F2" alt="NVIDIA DeepStream"/></td>
<td align="center"><img src="https://img.shields.io/badge/-NVIDIA%20Jetson-1C1B19?style=flat-square&logo=nvidia&logoColor=F8F6F2" alt="NVIDIA Jetson"/></td>
</tr>
<tr>
<td align="center"><img src="https://img.shields.io/badge/-LangGraph-1C1B19?style=flat-square&logo=langgraph&logoColor=F8F6F2" alt="LangGraph"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Pydantic%20AI-1C1B19?style=flat-square&logo=pydantic&logoColor=F8F6F2" alt="Pydantic AI"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Opik-1C1B19?style=flat-square" alt="Opik"/></td>
<td align="center"><img src="https://img.shields.io/badge/-Weights%20%26%20Biases-1C1B19?style=flat-square&logo=weightsandbiases&logoColor=F8F6F2" alt="Weights & Biases"/></td>
<td align="center"><img src="https://img.shields.io/badge/-MLflow-1C1B19?style=flat-square&logo=mlflow&logoColor=F8F6F2" alt="MLflow"/></td>
<td align="center"><img src="https://img.shields.io/badge/-AzureML-1C1B19?style=flat-square" alt="AzureML"/></td>
</tr>
</table>

**Engineering**

<img src="https://skillicons.dev/icons?i=aws,azure,docker,kubernetes,fastapi,django,angular,redis,postgres,mongodb,grafana,prometheus,elasticsearch,jenkins,terraform,git,github,githubactions&theme=light" alt="AWS, Azure, Docker, Kubernetes, FastAPI, Django, Angular, Redis, PostgreSQL, MongoDB, Grafana, Prometheus, Elasticsearch, Jenkins, Terraform, Git, GitHub, GitHub Actions" />

Also in the rotation: AWS Lambda, ECS, and CDK; TeamCity; Splunk and Datadog; and daily-driver AI coding agents — Claude Code, Cursor, and GitHub Copilot.

<br/>

## Why follow

*We need less hype. More engineering.* If you're a software engineer trying to actually understand AI, not just call an API, here's what's in it for you:

- **[The AI Merge](https://theaimerge.com)** — field notes and deep dives on production AI systems, no prompt lists. Grew from ~300 to 10,000+ subscribers in a year.
- Early access to **The AI Atlas**, a 220+ slide visual guide to the whole AI stack — hardware, training, inference, agents, deployment
- An **NVIDIA content partnership** — tutorials on CUDA, TensorRT, NIM, RTX, plus hardware access via an NVIDIA DGX Spark
- A **YouTube channel** with system-design walkthroughs and live coding, not tutorials that stop at "hello world"

<br/>

---

<a href="https://theaimerge.com">
  <img src="./assets/cta-banner.svg?v=2" width="100%" alt="Become an AI Engineer — theaimerge.com" />
</a>

<table align="center" width="100%">
<tr>
<td width="25%" align="center"><a href="https://theaimerge.com"><img src="https://img.shields.io/badge/Visit-theaimerge.com-D95319?style=for-the-badge&logoColor=F8F6F2" /></a></td>
<td width="25%" align="center"><a href="https://read.theaimerge.com"><img src="https://img.shields.io/badge/Join-10%2C000%2B%20Engineers-1C1B19?style=for-the-badge" /></a></td>
<td width="25%" align="center"><a href="https://theaimerge.com"><img src="https://img.shields.io/badge/The%20AI%20Atlas-Join%20Waitlist-1C1B19?style=for-the-badge" /></a></td>
<td width="25%" align="center"><a href="https://www.youtube.com/@theaimerge"><img src="https://img.shields.io/badge/Watch-YouTube-1C1B19?style=for-the-badge&logo=youtube&logoColor=F8F6F2" /></a></td>
</tr>
</table>

<br/>

## Connect

<p align="center">
<a href="https://www.linkedin.com/in/arazvant/"><img src="https://img.shields.io/badge/-LinkedIn-1C1B19?style=flat-square" /></a>
<a href="https://theaimerge.com"><img src="https://img.shields.io/badge/-Website-1C1B19?style=flat-square" /></a>
<a href="mailto:alexandrurazvant@gmail.com"><img src="https://img.shields.io/badge/-Email-1C1B19?style=flat-square&logo=gmail&logoColor=F8F6F2" /></a>
<a href="https://medium.com/@arazvant"><img src="https://img.shields.io/badge/-Medium-1C1B19?style=flat-square&logo=medium&logoColor=F8F6F2" /></a>
<a href="https://twitter.com/RazvantAlexand"><img src="https://img.shields.io/badge/-X-1C1B19?style=flat-square&logo=x&logoColor=F8F6F2" /></a>
<a href="https://read.theaimerge.com"><img src="https://img.shields.io/badge/-Substack-1C1B19?style=flat-square&logo=substack&logoColor=F8F6F2" /></a>
<a href="https://www.youtube.com/@theaimerge"><img src="https://img.shields.io/badge/-YouTube-1C1B19?style=flat-square&logo=youtube&logoColor=F8F6F2" /></a>
<a href="https://github.com/the-ai-merge"><img src="https://img.shields.io/badge/-GitHub%20Org-1C1B19?style=flat-square&logo=github&logoColor=F8F6F2" /></a>
</p>

<br/>

<!-- <p align="center">
<img src="https://streak-stats.demolab.com/?user=arazvant&background=F8F6F2&border=E4E1DA&ring=D95319&fire=D95319&currStreakLabel=1C1B19&sideLabels=1C1B19&currStreakNum=1C1B19&sideNums=1C1B19&dates=A09F9A&stroke=E4E1DA" width="65%" alt="streak" />
</p> -->

<br/>

<p align="center">
  <img src="./assets/footer-rule.svg" width="100%" alt="" />
</p>
