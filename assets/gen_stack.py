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

TILE = 54
GLYPH = 28
GAP_X = 20
GAP_Y = 16
LABEL_H = 14
PAD = 22
PER_ROW = 10
FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"


def fetch_icon(slug):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, slug + ".svg")
    if not os.path.exists(path):
        url = "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/%s.svg" % slug
        urllib.request.urlretrieve(url, path)
    with open(path) as f:
        content = f.read()
    m = re.search(r'<path[^>]*\sd="([^"]+)"', content)
    if not m:
        raise ValueError("no path found for %s" % slug)
    return m.group(1)


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
                d = fetch_icon(slug)
                scale = GLYPH / 24.0
                gx = x + (TILE - GLYPH) / 2.0
                gy = y + (TILE - GLYPH) / 2.0
                parts.append(
                    '<g transform="translate(%.2f,%.2f) scale(%.4f)">'
                    '<path d="%s" fill="%s"/></g>' % (gx, gy, scale, d, CREAM)
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
    ("W&amp;B", "weightsandbiases", None),
    ("MLflow", "mlflow", None),
    ("AzureML", "microsoftazure", None),
]

ENGINEERING = [
    ("AWS", "amazonwebservices", None),
    ("Azure", "microsoftazure", None),
    ("Lambda", "awslambda", None),
    ("ECS", "amazonecs", None),
    ("AWS CDK", "amazonwebservices", None),
    ("Docker", "docker", None),
    ("Kubernetes", "kubernetes", None),
    ("Terraform", "terraform", None),
    ("FastAPI", "fastapi", None),
    ("Django", "django", None),
    ("Angular", "angular", None),
    ("PostgreSQL", "postgresql", None),
    ("Redis", "redis", None),
    ("MongoDB", "mongodb", None),
    ("Elasticsearch", "elasticsearch", None),
    ("Grafana", "grafana", None),
    ("Prometheus", "prometheus", None),
    ("Splunk", "splunk", None),
    ("Datadog", "datadog", None),
    ("Jenkins", "jenkins", None),
    ("TeamCity", "teamcity", None),
    ("Git", "git", None),
    ("Actions", "githubactions", None),
    ("Claude Code", "claude", None),
    ("Cursor", "cursor", None),
    ("Copilot", "githubcopilot", None),
]

if __name__ == "__main__":
    build(FOUNDATIONS, "stack-foundations.svg")
    build(SYSTEMS, "stack-systems.svg")
    build(ENGINEERING, "stack-engineering.svg")
