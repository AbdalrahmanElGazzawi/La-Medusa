/* La Medusa — site configuration
   Phase 1: everything routes to WhatsApp.
   Phase 2: flip bookingEnabled, set analytics IDs, point Supabase keys — no rebuild needed. */
window.LM_CONFIG = {
  whatsappNumber: "201156166225",
  instagram: {
    shala: "https://www.instagram.com/theaerialistshala/",
    mona: "https://www.instagram.com/yogawith_mona/",
    reem: "https://www.instagram.com/profoundlytrue/",
    hammocks: "https://www.instagram.com/hammocksbymonashafei/"
  },

  /* Analytics — paste IDs when ready; scripts only load if set. */
  ga4Id: "",            /* e.g. "G-XXXXXXXXXX" */
  metaPixelId: "",      /* e.g. "1234567890" */

  /* Phase 2 slots (booking, payments, inquiry forms) */
  bookingEnabled: false,
  supabaseUrl: "https://qpvykmqepyugqtbxzqnq.supabase.co",
  supabaseAnonKey: "sb_publishable_ReyYpPnyfXazqdTa7wClLQ_dOF4JrEo",

  /* Prefilled WhatsApp messages per CTA context (EN + AR) */
  waMessages: {
    en: {
      general: "AERIAL — Hi La Medusa! I found you through the website.",
      classes: "AERIAL — Hi! I'd like to book a class. Which sessions have space this week?",
      kids: "AERIAL — Hi! I'd like to ask about kids' aerial classes.",
      ayttc: "AYTTC — Hi! I'm interested in the July 2026 teacher training. Could you send me the details and how to reserve a spot?",
      retreat: "RETREAT — Hi! I'd like to hear about the next La Medusa retreat dates and pricing.",
      hammocks: "HAMMOCKS — Hi! I'd like to order a handmade hammock / see the catalog.",
      partner: "PARTNER — Hi! I'm reaching out about a partnership / corporate event.",
      access: "AERIAL — Hi! I'd like to ask about accessible / adapted classes."
    },
    ar: {
      general: "AERIAL — مرحباً لا ميدوزا! وصلت إليكم عبر الموقع.",
      classes: "AERIAL — مرحباً! أودّ حجز حصة. ما المواعيد المتاحة هذا الأسبوع؟",
      kids: "AERIAL — مرحباً! أودّ السؤال عن حصص الأطفال.",
      ayttc: "AYTTC — مرحباً! مهتمة بتدريب المعلمين لشهر يوليو ٢٠٢٦. هل يمكن إرسال التفاصيل وطريقة الحجز؟",
      retreat: "RETREAT — مرحباً! أودّ معرفة مواعيد وأسعار الريتريت القادم.",
      hammocks: "HAMMOCKS — مرحباً! أودّ طلب أرجوحة مصنوعة يدوياً / مشاهدة الكتالوج.",
      partner: "PARTNER — مرحباً! أتواصل بخصوص شراكة أو فعالية للشركات.",
      access: "AERIAL — مرحباً! أودّ السؤال عن الحصص المهيّأة لذوي الاحتياجات."
    }
  }
};
