"""Generate uniform tech-stack tile grids as self-hosted SVGs.

Every tile is the same size: charcoal rounded square, cream glyph (simple-icons)
or a cream monogram when no official logo exists, with a label underneath.
"""
import os
import re
import urllib.request

CREAM = "#F8F6F2"
CHARCOAL = "#1C1B19"
TERRACOTTA = "#D95319"
MUTED = "#6B6960"

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".icon_cache")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

TILE = 46
GLYPH = 24
GAP_X = 14
GAP_Y = 14
LABEL_H = 14
PAD = 20
PER_ROW = 12
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


def fetch_icon(spec):
    """Fetch an icon by spec and return (path_d_list, (minx, miny, w, h)).

    spec is either a bare simple-icons slug ("python"), or prefixed:
      "si:<slug>"          simple-icons  (24x24 viewBox)
      "dv:<name>-<variant> devicon       (usually 128x128)
    """
    if spec.startswith("dv:"):
        name = spec[3:]
        base = name.rsplit("-", 1)[0]
        url = (
            "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/%s/%s.svg"
            % (base, name)
        )
        cache_key = "dv_" + name
    else:
        slug = spec[3:] if spec.startswith("si:") else spec
        url = "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/%s.svg" % slug
        cache_key = "si_" + slug

    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, cache_key + ".svg")
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    with open(path) as f:
        content = f.read()

    paths = re.findall(r'<path[^>]*\sd="([^"]+)"', content)
    if not paths:
        raise ValueError("no path found for %s" % spec)

    vb = re.search(r'viewBox="([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)"', content)
    box = tuple(float(v) for v in vb.groups()) if vb else (0.0, 0.0, 24.0, 24.0)
    return paths, box


def monogram_size(text):
    return {1: 21, 2: 17, 3: 13}.get(len(text), 11)


def build(items, out_name):
    """items: list of (label, slug_or_None, monogram_or_None)"""
    rows = [items[i : i + PER_ROW] for i in range(0, len(items), PER_ROW)]
    cell_w = TILE + GAP_X
    cell_h = TILE + LABEL_H + GAP_Y
    # Fixed panel width regardless of item count, so tiles render at the same
    # scale in every ladder when the images sit side by side in the README.
    width = PAD * 2 + cell_w * PER_ROW - GAP_X
    height = PAD * 2 + cell_h * len(rows) - GAP_Y

    parts = [
        '<svg width="%d" height="%d" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'
        % (width, height, width, height),
        '<rect width="%d" height="%d" rx="16" fill="%s"/>' % (width, height, CREAM),
    ]

    for r, row in enumerate(rows):
        for c, (label, slug, mono) in enumerate(row):
            x = PAD + c * cell_w
            y = PAD + r * cell_h
            parts.append(
                '<rect x="%d" y="%d" width="%d" height="%d" rx="12" fill="%s"/>'
                % (x, y, TILE, TILE, CHARCOAL)
            )
            if slug:
                paths, (bx, by, bw, bh) = fetch_icon(slug)
                edge = max(bw, bh)
                scale = GLYPH / edge
                # centre the icon's own box inside the tile
                gx = x + (TILE - bw * scale) / 2.0 - bx * scale
                gy = y + (TILE - bh * scale) / 2.0 - by * scale
                glyphs = "".join(
                    '<path d="%s" fill="%s"/>' % (d, CREAM) for d in paths
                )
                parts.append(
                    '<g transform="translate(%.2f,%.2f) scale(%.4f)">%s</g>'
                    % (gx, gy, scale, glyphs)
                )
            else:
                parts.append(
                    '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" '
                    'font-weight="700" font-size="%d" fill="%s">%s</text>'
                    % (
                        x + TILE / 2.0,
                        y + TILE / 2.0 + monogram_size(mono) * 0.36,
                        FONT,
                        monogram_size(mono),
                        CREAM,
                        mono,
                    )
                )
            parts.append(
                '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" '
                'font-weight="500" font-size="10" fill="%s">%s</text>'
                % (x + TILE / 2.0, y + TILE + 12, FONT, MUTED, label)
            )

    parts.append("</svg>")
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, out_name)
    with open(out, "w") as f:
        f.write("\n".join(parts) + "\n")
    print("wrote %s (%dx%d, %d tiles)" % (out, width, height, len(items)))


FOUNDATIONS = [
    ("Python", "python", None),
    ("Go", "go", None),
    ("Kotlin", "kotlin", None),
    ("C++", "cplusplus", None),
    ("Rust", "rust", None),
    ("PyTorch", "pytorch", None),
    ("TensorFlow", "tensorflow", None),
    ("scikit-learn", "scikitlearn", None),
]

SYSTEMS = [
    ("CUDA", "nvidia", None),
    ("TensorRT", "nvidia", None),
    ("Triton", "nvidia", None),
    ("DeepStream", "nvidia", None),
    ("Jetson", "nvidia", None),
    ("vLLM", "vllm", None),
    ("ONNX", "onnx", None),
    ("HuggingFace", "huggingface", None),
    ("OpenCV", "opencv", None),
    ("Qdrant", "qdrant", None),
    ("LangChain", "langchain", None),
    ("LangGraph", "langgraph", None),
    ("Pydantic AI", "pydantic", None),
    ("MCP", "modelcontextprotocol", None),
    ("Ollama", "ollama", None),
    ("NeMo", "nvidia", None),
    ("Ray", "ray", None),
    ("Core ML", "apple", None),
    ("pgvector", "postgresql", None),
    ("W&amp;B", "weightsandbiases", None),
    ("MLflow", "mlflow", None),
    ("LangSmith", "langchain", None),
    ("Logfire", "pydantic", None),
    ("AzureML", "microsoftazure", None),
]

ENGINEERING = [
    ("AWS", "amazonwebservices", None),
    ("Azure", "microsoftazure", None),
    ("Lambda", "awslambda", None),
    ("ECS", "amazonecs", None),
    ("AWS CDK", "amazonwebservices", None),
    ("AWS IoT", "amazonwebservices", None),
    ("Docker", "docker", None),
    ("Kubernetes", "kubernetes", None),
    ("Terraform", "terraform", None),
    ("FastAPI", "fastapi", None),
    ("Django", "django", None),
    ("Angular", "angular", None),
    ("PostgreSQL", "postgresql", None),
    ("Redis", "redis", None),
    ("MongoDB", "mongodb", None),
    ("Elastic", "elasticsearch", None),
    ("Grafana", "grafana", None),
    ("Prometheus", "prometheus", None),
    ("Splunk", "splunk", None),
    ("Datadog", "datadog", None),
    ("Jenkins", "jenkins", None),
    ("TeamCity", "teamcity", None),
    ("Kafka", "apachekafka", None),
    ("Airflow", "apacheairflow", None),
    ("OpenSearch", "opensearch", None),
    ("OTel", "opentelemetry", None),
    ("gRPC", "dv:grpc-plain", None),
    ("NATS", "natsdotio", None),
    ("WebRTC", "webrtc", None),
    ("Istio", "istio", None),
    ("Envoy", "envoyproxy", None),
    ("GStreamer", "gstreamer", None),
    ("FFmpeg", "ffmpeg", None),
    ("Argo CD", "argo", None),
    ("Helm", "helm", None),
    ("DVC", "dvc", None),
    ("Git", "git", None),
    ("Actions", "githubactions", None),
    ("Claude Code", "claude", None),
    ("Cursor", "cursor", None),
]

if __name__ == "__main__":
    build(FOUNDATIONS, "stack-foundations.svg")
    build(SYSTEMS, "stack-systems.svg")
    build(ENGINEERING, "stack-engineering.svg")
