# Builds docs/kestrel_air_policies.pdf: a FICTIONAL airline handbook (made up for this video).
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
st = getSampleStyleSheet()
PAGES = [
 ("Kestrel Air Customer Policies (fictional, 2026 edition)", [
  ("1. About this handbook", "Kestrel Air is a fictional airline invented for a tutorial. This handbook explains our rules for tickets, refunds, baggage, pets and special fares. If anything on our website or in a chat conflicts with this handbook, this handbook wins."),
  ("2. Ticket changes", "Economy Light tickets cannot be changed. Economy Flex tickets can be changed up to 3 hours before departure with no change fee; you only pay any fare difference. Business tickets can be changed at any time, including after the flight has departed, within 30 days."),
  ("3. Cancellations and refunds", "Economy Light tickets are non-refundable, but taxes are refunded on request. Economy Flex and Business tickets can be cancelled for a full refund up to 24 hours before departure. Refunds are paid to the original card within 10 business days."),
 ]),
 ("Special fares", [
  ("4. Bereavement fares", "If you must travel because of the death or imminent death of an immediate family member, Kestrel Air offers a bereavement fare that is 30% off the Economy Flex price. The bereavement fare must be requested BEFORE you travel, by calling our care team at +1 555 0142. Bereavement discounts cannot be applied retroactively: we do not refund the difference for trips that have already been taken. You will be asked for a death certificate or a letter from a hospital within 14 days of booking."),
  ("5. Student fares", "Students aged 16 to 26 get 10% off Economy Flex with a valid student card. The discount does not combine with other offers."),
  ("6. Medical travel", "Passengers who need oxygen must tell us at least 72 hours before departure. Kestrel Air provides approved portable oxygen concentrators free of charge on flights longer than 2 hours."),
 ]),
 ("Baggage and pets", [
  ("7. Cabin baggage", "Every passenger may bring one cabin bag of up to 8 kg and 55 x 40 x 23 cm, plus one small personal item such as a laptop bag."),
  ("8. Checked baggage", "Economy Light includes no checked bag. Economy Flex includes one checked bag of up to 23 kg. Business includes two checked bags of up to 32 kg each. Extra bags cost $45 each when added online and $70 at the airport."),
  ("9. Travelling with pets", "Small cats and dogs may travel in the cabin if the animal and its carrier together weigh no more than 7 kg. The carrier must fit under the seat in front of you. The pet fee is $60 per flight, and a maximum of two pets are allowed per flight, so book early. Larger animals travel in the hold as cargo."),
 ]),
 ("Delays and contact", [
  ("10. Delays", "If your flight is delayed by more than 4 hours, Kestrel Air gives you a meal voucher worth $15. If it is delayed by more than 8 hours overnight, we provide a hotel room and transport."),
  ("11. Wi-Fi on board", "Wi-Fi is free for messaging on all aircraft. Full browsing costs $8 per flight, and it is free for Business passengers."),
  ("12. Contact", "Our care team is available 24/7 at +1 555 0142 or care@kestrel-air.example. The chat assistant on our website answers from this handbook only."),
 ]),
]
doc = SimpleDocTemplate("docs/kestrel_air_policies.pdf", pagesize=A4, title="Kestrel Air Customer Policies (fictional)")
flow = []
for i, (title, secs) in enumerate(PAGES):
    flow.append(Paragraph(title, st["Title"] if i == 0 else st["Heading1"]))
    for h, body in secs:
        flow += [Paragraph(h, st["Heading2"]), Paragraph(body, st["BodyText"]), Spacer(1, 8)]
    if i < len(PAGES) - 1: flow.append(PageBreak())
doc.build(flow); print("wrote docs/kestrel_air_policies.pdf,", len(PAGES), "pages")
