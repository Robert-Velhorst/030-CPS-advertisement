# CPS Advertisement

CPS Advertisement is a market-access and financing platform for freelancers, start-ups, and small businesses with no more than **€100,000 in annual gross revenue**.

Its purpose is to make reliable digital promotion available without requiring the seller to risk advertising money upfront. Sellers pay only after verified sales. Every eligible and valid campaign receives a meaningful minimum market test, while campaigns that continue producing profitable sales may scale without a predetermined reach ceiling.

The first version finances this guaranteed exposure through voluntarily contributed computing power, successful-sale commissions, and integrations with existing advertising, affiliate, creator, publisher, and distributed-compute platforms.

> **Core principle:** Convert idle computing power and successful-sale commissions into guaranteed market access for small parties. Do not make the people who most need an opportunity carry the upfront advertising risk.

## Why this product should exist

Traditional digital advertising asks a seller to pay before knowing whether a market exists. This is particularly difficult for:

- freelancers;
- self-employed professionals;
- new businesses;
- niche-product creators;
- local or geographically specialized businesses;
- businesses considering entry into a new region;
- people with a useful offer but little working capital.

These sellers are often expected to perform extensive market research and then risk scarce money on impressions or clicks. A market may also be created through exposure rather than merely discovered in advance.

CPS Advertisement reverses that sequence:

1. An eligible seller submits a lawful, deliverable, and measurable offer.
2. The platform guarantees a transparent minimum market test.
3. The seller incurs no advertising charge if no verified sale occurs.
4. A dynamic commission becomes payable only after a sale is verified.
5. Continued sales progressively unlock more distribution.
6. Successful campaigns may scale without a predetermined reach cap.
7. Campaigns that do not sell can be revised and tested again without creating advertising debt.

Real purchasing behavior, not a centralized prediction about whether a product deserves a market, determines continued distribution.

## Product position

CPS Advertisement is not intended to recreate Google, Meta, affiliate networks, compute marketplaces, or a complete advertising exchange.

It is an **integration, underwriting, guarantee, attribution, and settlement layer** above existing infrastructure.

The platform should integrate, where technically and contractually possible, with:

- Google Ads and the Google Ads API;
- Meta advertising and the Meta Conversions API;
- affiliate and partnership networks;
- creator and influencer marketplaces;
- publisher and newsletter networks;
- e-commerce and payment platforms;
- distributed CPU and GPU marketplaces;
- additional authorized advertising channels.

Relevant existing capabilities include:

- Google Ads API supports a pay-per-conversion payment mode for eligible Display campaigns with specific campaign settings.
- Meta's Conversions API can send purchase and other outcome data for measurement and optimization, although it does not itself convert standard Meta billing into CPS.
- Partnership platforms such as impact.com already provide e-commerce integrations, product feeds, tracking, contracting, and clearinghouse functionality.
- Distributed-compute networks such as Golem demonstrate that participants can provide computing resources and receive compensation.

Official references:

- [Google Ads API payment modes](https://developers.google.com/google-ads/api/reference/rpc/v24/PaymentModeEnum.PaymentMode)
- [Meta Conversions API](https://www.facebook.com/business/help/AboutConversionsAPI)
- [impact.com partnership platform](https://impact.com/integrated-platform-prices/)
- [Golem provider documentation](https://docs.golem.network/docs/providers/provider-installation)

All integrations must follow the applicable platform terms, privacy requirements, API restrictions, and financial regulations.

## Target beneficiaries

Subsidized CPS market access is available only to parties whose total annual gross business revenue does not exceed **€100,000**.

Eligible beneficiaries include:

- freelancers;
- sole proprietors;
- new businesses with no historical revenue;
- small companies;
- small non-profit or mission-driven trading entities where permitted;
- connected small businesses whose aggregated revenue remains within the limit.

Large organizations may contribute compute, money, services, publisher inventory, or sponsorship. They may not use the subsidized market-access programme for their own campaigns.

### Revenue qualification

The initial policy uses total gross business revenue over the most recent rolling twelve months.

The system must support:

- seller self-declaration;
- evidence from bookkeeping, tax records, payment providers, or commerce platforms;
- periodic re-verification;
- aggregation of businesses under the same ultimate beneficial owner when needed to prevent artificial splitting;
- a documented review and appeal process;
- data minimization and protected storage of verification evidence;
- orderly completion of existing sales, returns, and settlements after a seller becomes ineligible.

The revenue ceiling is a programme eligibility rule, not a judgement about product quality.

## Open market-access principle

CPS Advertisement must not operate as a subjective committee deciding which ideas deserve market access.

A campaign may be prevented from running only when necessary, including:

- the offer is illegal;
- product or advertising claims are materially deceptive;
- the product cannot reasonably be delivered;
- a sale cannot be reliably measured;
- required consumer protections are absent;
- fraud or sanctions risks cannot be controlled;
- an external distribution partner lawfully prohibits the category;
- the campaign violates an applicable platform policy.

The system may calculate risk and adapt test conditions, but it must explain its rules. Higher uncertainty should ordinarily produce a smaller first experiment, a different channel mix, a longer settlement reserve, or increased verification—not ideological exclusion.

## Reach commitment

Literal unlimited guaranteed reach is impossible because advertising inventory and human attention are finite. CPS Advertisement therefore combines two commitments.

### Guaranteed minimum exposure

Every eligible and valid campaign receives a **Guaranteed Discovery Allocation**.

The allocation must:

- represent a meaningful market test;
- be shown to the seller before activation;
- specify the measurement unit, such as qualified impressions, placements, active distribution days, or a justified combination;
- be targeted only to plausibly relevant contexts or audiences;
- be tracked in a dedicated ledger;
- show promised, delivered, invalidated, and remaining exposure;
- distinguish purchased, partner-contributed, and subsidized exposure;
- remain configurable by geography, category, product type, and available funding.

The guarantee is an actual distribution commitment, not merely a listing in a campaign catalogue.

### No predetermined ceiling after sales

When verified sales demonstrate that the agreed CPS commission can support additional distribution, the platform should continue increasing reach while:

- compliant inventory remains available;
- marginal performance remains economically supportable;
- product supply remains available;
- returns and fraud remain acceptable;
- the seller continues to accept the disclosed commission terms.

The platform does not promise infinite impressions. It promises that a successful campaign will not be stopped because it reached an arbitrary fixed advertising quota.

## Version 1 overview

Version 1 consists of two inseparable modules:

1. **Compute Funding Module**
2. **Guaranteed CPS Advertising Module**

The financing module is part of the first product, not a later enhancement.

### Version 1 dependency

Compute has monetary value only when useful workloads are available and the resulting compensation can be settled. Therefore, Version 1 must integrate with at least one approved existing compute marketplace or contracted compute buyer before it can promise funded advertising.

The platform must never issue guaranteed advertising credits based only on theoretical compute availability. Credits become funded when compute work is verified and its proceeds are settled, or when an approved reserve explicitly underwrites them.

## Compute Funding Module

The Compute Funding Module converts voluntarily supplied idle computing capacity into value for the CPS Discovery Fund.

### Contributors

Compute may be contributed by:

- individuals;
- beneficiary sellers;
- supporters sponsoring a seller or campaign;
- businesses donating idle capacity;
- institutions;
- community organisations;
- server operators.

A beneficiary is not required to contribute personal computing power. This prevents the opportunity cost from being shifted back to the small party seeking access.

### Provider-neutral adapter model

CPS Advertisement must not build a complete compute marketplace in Version 1.

It should implement a provider-neutral adapter interface supporting:

- contributor identity mapping;
- node registration or linked marketplace accounts;
- hardware capability and benchmark metadata;
- work availability;
- completed-work evidence;
- gross proceeds;
- provider fees;
- settlement status;
- currency or asset conversion;
- contributor allocation instructions;
- reconciliation and dispute states.

Each compute provider integration must be isolated so it can be replaced without changing advertising or settlement logic.

### Contribution allocations

A contributor may direct settled compute value to:

- the general CPS Discovery Fund;
- a specific eligible seller;
- a specific eligible campaign;
- a defined category, region, or community programme;
- the contributor's own eligible campaign;
- a permitted withdrawal option when offered.

The platform must clearly distinguish donation, restricted sponsorship, campaign credit, and withdrawable contributor earnings.

### Safe node operation

If CPS distributes its own node software, it must provide:

- explicit opt-in;
- visible start, pause, scheduling, and uninstall controls;
- user-defined CPU, GPU, memory, storage, time, temperature, and power limits;
- optional operation only while idle or connected to mains power;
- realtime workload and earnings visibility;
- signed software and signed workload manifests;
- strong workload isolation;
- no access to unrelated personal files;
- no hidden cryptocurrency mining;
- no silent mobile battery usage;
- clear electricity-cost and hardware-wear disclosures;
- automatic shutdown on thermal, battery, integrity, or policy violations;
- an auditable update mechanism;
- security review before public distribution.

Phone participation may be investigated, but Version 1 must not assume that ordinary smartphones can provide economical or platform-permitted background compute.

### Compute valuation

Credits must reflect settled economic value, not raw online time.

The valuation engine should record:

- provider;
- workload type;
- hardware type;
- benchmarked performance;
- completed compute units;
- gross compensation;
- marketplace and conversion fees;
- settlement currency or asset;
- exchange rate and timestamp where conversion is required;
- net amount allocated to advertising;
- reversals or disputes.

The UI must not imply guaranteed compute earnings.

## CPS Discovery Fund

The CPS Discovery Fund finances guaranteed market tests.

Funding sources may include:

- settled compute proceeds;
- a reserved portion of commissions from successful sales;
- voluntary sponsorship;
- partner-contributed media inventory;
- grants or investment allocated for discovery;
- recoveries from valid fraud or chargeback claims.

The ledger must separate:

- available cash or cash-equivalent funding;
- restricted sponsorship;
- unsettled compute proceeds;
- advertising credits;
- committed but undelivered exposure;
- reserves for returns, disputes, taxes, and platform fees.

No campaign guarantee may be issued without an identified funding source and sufficient available reserve.

## Guaranteed CPS Advertising Module

### Seller onboarding

The seller provides:

- legal or trading identity;
- beneficiary eligibility evidence;
- product or service details;
- sale price;
- gross margin information;
- tax and delivery regions;
- inventory or capacity;
- fulfilment times;
- return and cancellation terms;
- product claims and required evidence;
- connected commerce, payment, or booking systems;
- maximum acceptable commission per verified sale;
- campaign assets or source materials;
- excluded channels, audiences, or geographies.

### Campaign routing

The campaign router distributes the Guaranteed Discovery Allocation across authorized existing channels.

Routing should consider:

- channel eligibility;
- geographic availability;
- contextual relevance;
- expected commission value;
- available discovery funding;
- publisher or partner terms;
- historical conversion and return data;
- inventory and seller capacity;
- channel-specific tracking quality;
- the need to give new campaigns a genuine test.

The router must not allow established winners to consume all discovery capacity. A configurable portion of funded exposure must remain available for new campaigns.

### Existing-platform integrations

Connectors should support, where officially available:

- campaign creation and updates;
- product feeds;
- creative assets;
- budget or commission configuration;
- placement and delivery data;
- clicks and impression reporting;
- conversion events;
- cancellation and refund events;
- partner or publisher identity;
- fees and invoices;
- deep links to source-platform records;
- rate-limit and permission handling.

A connector must never claim to provide true CPS billing when the external platform still charges for impressions or clicks. In those cases, the Discovery Fund underwrites the media cost and the seller remains protected from upfront billing.

## Dynamic CPS calculation

The platform calculates a transparent per-sale commission proposal using:

- sale price;
- gross margin;
- applicable taxes;
- payment processing costs;
- average fulfilment cost where relevant;
- expected return and cancellation rates;
- fraud and chargeback risk;
- channel fees;
- required market-test cost;
- expected conversion range;
- reserve requirements;
- CPS platform fee;
- contribution to the Discovery Fund.

The seller sets the maximum acceptable commission. The system must not activate a campaign under terms that exceed that limit.

The final value may be:

- a fixed amount per verified sale;
- a percentage of recognized sale value;
- a tiered amount based on product, order value, or customer type;
- a hybrid formula disclosed before activation.

All calculations must be versioned and reproducible.

## Sale attribution and verification

A sale becomes commissionable only when it meets the defined verification policy.

The platform must support:

- signed conversion events;
- server-to-server commerce and payment webhooks;
- campaign, click, referral, and order identifiers;
- configurable attribution windows;
- duplicate-event prevention;
- consent and privacy signals;
- cancellation, return, chargeback, and partial-refund handling;
- fraud scoring;
- manual review with audit trails;
- source-platform reconciliation;
- final settlement after the applicable confirmation or return period.

AI may assist fraud review, but it must not autonomously deny money without explainable evidence and an appeal path.

## Commission settlement

After a verified and final sale, the commission may be distributed among:

- the advertising platform or publisher;
- an affiliate, creator, or referral partner;
- CPS Advertisement;
- the CPS Discovery Fund;
- attribution, payment, and compliance providers;
- applicable tax or reserve accounts.

The exact split must be disclosed and recorded before campaign activation.

Settlement requires:

- double-entry or equivalently auditable accounting;
- immutable transaction identifiers;
- idempotent processing;
- balance reconciliation;
- reversal handling;
- tax and invoice records;
- segregation of restricted or client funds where legally required;
- payout thresholds and status visibility;
- dispute and appeal procedures.

Financial architecture must receive professional legal, accounting, tax, payments, and regulatory review before live public use.

## Primary user roles

### Beneficiary seller

Can:

- verify eligibility;
- connect sales systems;
- submit and manage campaigns;
- view guaranteed and delivered exposure;
- accept or reject CPS terms;
- inspect attribution and sales;
- manage product capacity;
- dispute classifications or transactions;
- revise and retest campaigns.

### Compute contributor

Can:

- link or operate provider nodes;
- view verified work and settled proceeds;
- set contribution allocations;
- control resources and schedules;
- see electricity and device-impact disclosures;
- pause or leave;
- dispute missing work or value.

### Sponsor

Can allocate money, compute proceeds, or media inventory to eligible campaigns or defined programmes without receiving hidden control over campaign content.

### Distribution partner

Can expose authorized inventory, receive campaigns, report delivery and conversions, and receive agreed CPS compensation.

### Platform operator

Can manage integrations, reconciliation, legal restrictions, security incidents, verified fraud, and appeals. The operator must not perform subjective ideological product selection.

### Auditor or compliance reviewer

Receives controlled access to evidence, calculations, settlements, policy decisions, and security logs without unnecessary exposure to personal data.

## Suggested architecture

Keep the system modular:

1. **Identity and eligibility service**
2. **Seller and product service**
3. **Campaign and guarantee service**
4. **Compute-provider adapters**
5. **Compute valuation and allocation service**
6. **Discovery Fund ledger**
7. **Advertising and affiliate connectors**
8. **Campaign routing service**
9. **Conversion and attribution service**
10. **Risk, fraud, return, and dispute service**
11. **Dynamic CPS calculator**
12. **Settlement and reconciliation service**
13. **Seller, contributor, partner, and operator dashboards**
14. **Audit, privacy, consent, and policy service**

Every external integration must communicate through a documented adapter contract. Financial state changes should be event-driven, idempotent, and independently auditable.

## Core data entities

The initial data model should include:

- User
- Organisation
- BeneficialOwner
- EligibilityAssessment
- RevenueEvidence
- Seller
- Product
- Offer
- Campaign
- CampaignTermsVersion
- GuaranteedDiscoveryAllocation
- ExposureDelivery
- DistributionChannel
- DistributionPartner
- ComputeContributor
- ComputeNode
- ComputeProvider
- ComputeWorkRecord
- ComputeSettlement
- ContributionAllocation
- DiscoveryFundAccount
- LedgerEntry
- ConversionEvent
- AttributionRecord
- Sale
- Return
- Chargeback
- Commission
- Payout
- Reserve
- Dispute
- AuditEvent
- ConsentRecord

Money values must use integer minor units plus currency codes. Rates and exchange conversions must retain precision and source timestamps.

## Failure handling

The system must fail safely and visibly.

Examples:

- Unsettled compute proceeds do not create spendable advertising credits.
- A disconnected compute provider is shown as unavailable.
- A disconnected advertising channel stops new routing without losing campaign history.
- Missing conversion verification delays settlement instead of guessing.
- Duplicate webhooks do not duplicate sales or payouts.
- A platform rate limit triggers documented backoff.
- Reversed sales reverse only the affected provisional balances.
- A depleted Discovery Fund prevents new promises but does not erase existing commitments.
- An ineligible seller cannot create new subsidized campaigns but can complete existing obligations.
- A failed eligibility check identifies the missing evidence and provides review options.
- Unsupported channels are labelled accurately rather than simulated through unauthorized automation.

## Security and privacy requirements

At minimum:

- strong authentication and role-based authorization;
- secure storage and rotation of external API credentials;
- encryption in transit and at rest;
- separation of identity, eligibility evidence, campaign data, and financial data;
- signed webhook verification;
- least-privilege connector scopes;
- tamper-evident audit logs;
- rate limiting and abuse controls;
- data retention, export, correction, and deletion workflows;
- incident response and provider revocation procedures;
- GDPR and ePrivacy assessment for European operation;
- payment, tax, consumer-protection, sanctions, and platform-policy review;
- no sale of personal data;
- no hidden behavioral profiling;
- contextual targeting preferred where practical;
- explicit consent for optional tracking and compute participation.

## Version 1 functional scope

Version 1 should demonstrate an end-to-end, economically real flow:

1. Verify that a seller is within the €100,000 annual revenue limit.
2. Connect at least one commerce or payment source.
3. Register a lawful and measurable offer.
4. Connect at least one distributed-compute provider or contracted compute buyer.
5. Import verified settled compute proceeds.
6. Allocate those proceeds to the Discovery Fund or a specific eligible campaign.
7. Connect at least one authorized advertising or affiliate channel.
8. Calculate and present dynamic CPS terms.
9. Issue a funded Guaranteed Discovery Allocation.
10. Deliver and measure actual exposure.
11. Receive and attribute a real or controlled-pilot sale.
12. process the confirmation or return period.
13. Settle the commission and replenish the Discovery Fund according to the agreed split.
14. Display the complete audit trail to authorized users.

## Version 1 acceptance criteria

Version 1 is acceptable when:

- a beneficiary above the revenue limit cannot receive a new subsidized allocation;
- an eligible new business with no revenue can qualify;
- connected-entity checks are represented in the eligibility model;
- compute value is not spendable before settlement;
- contributors can control or stop participation;
- a contributor can allocate value without being the campaign beneficiary;
- at least one real compute-provider adapter completes reconciliation;
- at least one authorized distribution connector reports delivery;
- every campaign promise identifies its funding source;
- guaranteed exposure is measurable and its remaining balance is visible;
- the seller incurs no advertising charge when no verified sale occurs;
- a sale cannot be paid twice;
- cancellations, returns, and chargebacks update provisional and final balances correctly;
- CPS calculations are reproducible from the stored terms version;
- commission recipients and fund contributions match the accepted terms;
- prohibited or unverifiable campaigns receive a specific, appealable reason;
- external platform limitations are accurately disclosed;
- audit records reconstruct the full compute-to-advertising-to-sale value chain.

## Product success measures

Measure whether CPS Advertisement:

- increases the number of small parties able to run a real market test;
- reduces upfront advertising expenditure for beneficiaries;
- delivers the promised minimum exposure;
- converts compute proceeds into verified advertising value efficiently;
- produces additional verified sales;
- supports repeatable profitable scaling;
- minimizes fraud, duplicate attribution, and settlement errors;
- keeps returns and chargebacks within sustainable limits;
- shortens the time from offer submission to first market exposure;
- enables specialisation or geographic entry that would otherwise be financially impractical;
- maintains contributor, seller, and distribution-partner trust.

## Out of scope for Version 1

- Building a complete replacement for Google Ads or Meta Ads.
- Building a global publisher network from scratch.
- Creating a general-purpose compute marketplace.
- Promising theoretical or unfunded advertising credits.
- Guaranteed sales.
- Literal infinite reach.
- Subsidized campaigns for businesses above €100,000 annual gross revenue.
- Hidden mining or involuntary device usage.
- Autonomous rejection based solely on opaque AI scoring.
- Unsupported circumvention of advertising-platform rules.
- Consumer lending or speculative financial products.

## Roadmap

### Phase 1: Funded pilot

Deliver the complete Version 1 flow with a small number of approved external integrations, controlled exposure guarantees, real accounting, and eligible pilot sellers.

### Phase 2: Integration expansion

Add more compute providers, advertising platforms, affiliate networks, commerce systems, publishers, creators, currencies, and jurisdictions.

### Phase 3: Automated portfolio scaling

Improve cross-channel routing, portfolio risk management, adaptive guarantees, fraud controls, and automatic scaling for campaigns with verified sustainable sales.

### Phase 4: Partner underwriting

Negotiate with Google, Meta, affiliate networks, publishers, compute providers, and other distribution partners to contribute exposure or carry CPS media risk directly.

### Phase 5: Open interoperability

Publish appropriate adapter specifications, transparency data, and governance rules so additional networks can interoperate without CPS Advertisement becoming an unavoidable centralized gatekeeper.

## Non-negotiable development principles

- Beneficiaries pay only after verified sales.
- Compute funding is part of Version 1.
- Beneficiaries are limited to no more than €100,000 annual gross revenue.
- Every campaign guarantee must be funded and measurable.
- A beneficiary need not contribute personal compute.
- No subjective ideological gatekeeping.
- Every restriction, calculation, and transaction must be explainable and appealable.
- Use existing infrastructure before building replacements.
- Never misrepresent an external platform's billing model.
- Never create credits from unverified theoretical value.
- Protect contributors' devices, privacy, and informed choice.
- Optimize for real market access, traceability, and sustainable win-win economics.
