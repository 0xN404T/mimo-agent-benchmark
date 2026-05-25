export default async function handler(req, res) {
  const input = (req.body && req.body.input) || "";
  const hasKey = Boolean(process.env.MIMO_API_KEY);
  const mode = hasKey ? "mimo-ready" : "mock-demo";
  const project = "mimo-agent-benchmark";
  const task = "benchmark";
  const mock = {"score": 0.82, "latency_ms": 1240, "expected_fix": "function add(a,b){ return a+b }", "notes": "Model should identify subtraction bug and preserve function signature."};
  return res.status(200).json({
    ok: true,
    project,
    task,
    mode,
    input_preview: input.slice(0, 500),
    result: mock,
    next_step: hasKey ? "Connect live MiMo request in this API route." : "Set MIMO_API_KEY in Vercel Environment Variables to enable real MiMo calls."
  });
}
