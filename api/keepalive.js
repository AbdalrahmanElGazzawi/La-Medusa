// Daily Supabase keepalive — a single REST read counts as project activity,
// which prevents the free-tier auto-pause. Wired to Vercel Cron in vercel.json.
export default async function handler(req, res) {
  const r = await fetch(
    "https://qpvykmqepyugqtbxzqnq.supabase.co/rest/v1/schedule_slots?select=id&limit=1",
    { headers: { apikey: "sb_publishable_ReyYpPnyfXazqdTa7wClLQ_dOF4JrEo" } }
  );
  res.status(r.ok ? 200 : 502).json({ ok: r.ok, at: new Date().toISOString() });
}
