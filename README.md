<!--
  README for github.com/arazvant
  Palette from theaimerge.com: cream #F8F6F2, charcoal #1C1B19, terracotta #D95319.
  assets/header.svg and assets/cta-banner.svg are hand-built — the header is an animated
  grid of squares, styled like a GitHub contribution graph, sweeping in left-to-right in
  brand colors. Self-hosted, no third-party generator. Bump the ?v= query after edits —
  raw.githubusercontent.com caches aggressively and won't otherwise pick up changes.
  assets/profile-photo.gif is the pixel-portrait GIF, resampled to 5fps.
  assets/stack-*.svg are the tech-stack tile grids — every tile the same size,
  charcoal on cream, real logos pulled from simple-icons (and devicon where
  simple-icons has no entry) via jsDelivr.
  Regenerate with: python3 assets/gen_stack.py (edit the lists in there).

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
<tr><td width="60%"><a href="https://github.com/the-ai-merge/multimodal-agents-course"><b>Kubrick</b></a> — an MCP-based multimodal AI agent with eyes and ears: vision, voice, and memory in one open-source course, built with Miguel Otero Pedrido</td><td align="right"><img src="https://img.shields.io/github/stars/the-ai-merge/multimodal-agents-course?style=flat-square&color=1C1B19&labelColor=F8F6F2" /></td></tr>
<tr><td><b>MAVS</b> — edge multi-agent vision system for wildlife conservation: an MLOps pipeline trains the CV models, then an MCP/A2A agentic layer runs them at the edge</td><td align="right"><sub>Soon</sub></td></tr>
<tr><td><b>Forge</b> — a human-gated SDLC for building with AI agents: you grill the spec, design, and plan; agents execute inside that scope through implement, review, and ship</td><td align="right"><sub>Soon</sub></td></tr>
<tr><td><b>Patch</b> — a local voice companion on an NVIDIA DGX Spark, with an iPhone as its mic and display: captures notes into Obsidian, runs Todoist, and handles daily focus/review routines</td><td align="right"><sub>Soon</sub></td></tr>
</table>

I like to think about Software and AI grouped in three ladders, which is the way I also teach it.

**Foundations**

<img src="./assets/stack-foundations.svg?v=2" width="100%" alt="Python, Go, Kotlin, C++, Rust, PyTorch, TensorFlow, scikit-learn" />

**Systems**

<img src="./assets/stack-systems.svg?v=3" width="100%" alt="CUDA, TensorRT, Triton, DeepStream, Jetson, vLLM, ONNX, HuggingFace, OpenCV, Qdrant, LangChain, LangGraph, Pydantic AI, MCP, Ollama, NeMo, Ray, Core ML, pgvector, Weights &amp; Biases, MLflow, LangSmith, Logfire, AzureML" />

**Engineering**

<img src="./assets/stack-engineering.svg?v=3" width="100%" alt="AWS, Azure, Lambda, ECS, AWS CDK, AWS IoT, Docker, Kubernetes, Terraform, FastAPI, Django, Angular, PostgreSQL, Redis, MongoDB, Elasticsearch, Grafana, Prometheus, Splunk, Datadog, Jenkins, TeamCity, Kafka, Airflow, OpenSearch, OpenTelemetry, gRPC, NATS, WebRTC, Istio, Envoy, GStreamer, FFmpeg, Argo CD, Helm, DVC, Git, GitHub Actions, Claude Code, Cursor, Copilot" />

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
