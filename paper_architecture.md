# Arhitectura Paper: Securitatea Platformei Android

**Target:** 10 pagini (format A4, două coloane)
**Principiu:** "Mai puțin dar mai bine" - profunzime unde contează

---

## 📊 Distribuție Pagini (10 total)

### 📄 Pagina 1 - Titlu + Rezumat + Introducere [1 pag]
✅ **Status:** COMPLET
- Titlu + autori
- Cuvinte cheie (10 termeni)
- Rezumat (1 paragraf)
- **1.1 Context** (3 paragrafe)
- **1.2 Obiective și Motivație** (2 paragrafe + notă personală rooting)

---

### 📄 Pagini 2-3 - Cap 2: Arhitectura Android [1-1.5 pag]

**Obiectiv:** Fundație tehnică necesară, dar CONCIS

#### 2.1 Arhitectura Sistemului
✂️ **SCURTEAZĂ:** 1 paragraf/strat (5 paragrafe total, ~150 cuvinte)
- **Kernel Linux:** Managementul memoriei, procese, networking, drivere
- **Biblioteci Native:** libc, media, browser engine, OpenGL, SQLite
- **Mediul de Execuție (Dalvik/ART):** VM pentru bytecode, Zygote process
- **Framework Aplicații:** API-uri (View, Content Provider, Notification Manager)
- **Stratul Aplicații:** SMS, contacte, browser, email

#### 2.2 Mecanisme de Izolare
🔀 **COMBINĂ** 2.2.1 + 2.2.2 într-o singură subsecțiune:
- Procese separate + UID distinct per aplicație (1 paragraf combinat, ~100 cuvinte)

#### 2.3 Sistemul de Permisiuni și Semnarea Aplicațiilor
🔀 **COMBINĂ** 2.3.1 + 2.3.2:
- Permisiuni Android + semnare aplicații (1 paragraf combinat, ~120 cuvinte)

**Total Cap 2:** ~370-400 cuvinte = 1-1.5 pag

---

### 📄 Pagini 3-5 - Cap 3: Modelul de Securitate [2-2.5 pag]

⭐ **FOCUS PRINCIPAL** - Aici investim spațiul!

#### 3.1 Mecanisme de Bază
**DETALIAT:** 2-3 paragrafe per mecanism

**3.1.1 Sandboxing**
- Model Linux user permissions + izolare procese
- Un proces per aplicație, un UID/GID per aplicație
- File system permissions, no setuid
- Exemplu concret (2-3 paragrafe, ~200 cuvinte)

**3.1.2 Permisiuni**
- Declarație în AndroidManifest.xml
- Signature verification/user authorization la instalare
- Categorii: normale, dangerous, signature, signatureOrSystem
- Exemplu API protejate (camera, GPS, SMS, Bluetooth)
- Android 2.3+ restricții MODIFY_PHONE_STATE (2-3 paragrafe, ~200 cuvinte)

**3.1.3 Izolare de Procese și Fișiere**
- Kernel-level isolation
- Data files owned by UID/GID
- Inter-process communication (IPC) security (1-2 paragrafe, ~150 cuvinte)

#### 3.2 Extensii Moderne
**FOARTE DETALIAT:** Aici e valoarea principală

**3.2.1 SELinux / SEAndroid**
- Transplantarea SELinux pe Android
- MAC (Mandatory Access Control) vs DAC
- Politici SELinux pentru procese și fișiere
- **Proiectul SE Android (NSA):** previne root privilege escalation
- Impact asupra exploatărilor (3-4 paragrafe, ~250 cuvinte)

**3.2.2 Verified Boot**
- Chain of trust de la bootloader
- Verificarea integrității sistemului la pornire
- Detectarea modificărilor (2 paragrafe, ~150 cuvinte)

**3.2.3 Criptarea Datelor (FDE/FBE)**
- **FDE (Full Disk Encryption):** criptare completă
- **FBE (File-Based Encryption):** criptare per-fișier, Direct Boot
- Avantaje FBE vs FDE (2-3 paragrafe, ~200 cuvinte)

**3.2.4 Keystore & TEE**
- **Trusted Execution Environment:** izolare hardware pentru operații criptografice
- **Keystore:** managementul cheilor sensibile
- **Play Integrity API:** 🆕 verificare integritate dispozitiv (menționare că e nou și strict pentru banking/apps sensibile)
- Protecție împotriva root/custom ROM (2-3 paragrafe, ~200 cuvinte)

**Total Cap 3:** ~1,350-1,500 cuvinte = 2-2.5 pag

---

### 📄 Pagini 5-6 - Cap 4: Vulnerabilități și Vectori de Atac [1.5-2 pag]

**🔴 RESTRUCTURAT:** TIPURI de vulnerabilități tehnice (4.1-4.5) + vectori de atac practici (4.6-4.7)

**Obiectiv:** Taxonomie tehnică clară, concisă (~150-180 cuvinte per subcapitol)

#### PARTEA I: Vulnerabilități Tehnice

**4.1 Vulnerabilități de Memory Corruption**
- **Definiție:** Buffer overflow, use-after-free, integer overflow în cod C/C++
- **Manifestare:** Stagefright (2015) - integer overflow în libstagefright, RCE prin MMS
- **Soluții:** ASLR, DEP, stack canaries, CFI, media server sandboxing Android 8.0+
- (~150-180 cuvinte, 1 paragraf compact)

**4.2 Vulnerabilități de Logic și Race Conditions**
- **Definiție:** TOCTOU, race conditions în kernel/drivers, improper synchronization
- **Manifestare:** QuadRooter (2016) - race în Qualcomm KGSL driver → root escalation
- **Soluții:** Kernel hardening, CFI, atomic operations, proper locking mechanisms
- (~150-180 cuvinte, 1 paragraf compact)

**4.3 Vulnerabilități în Permission Model**
- **Definiție:** Permission bypass, confused deputy, intent hijacking, component exposure
- **Manifestare:** Apps obțin date fără permisiuni, intent spoofing, IPC abuse
- **Soluții:** SELinux policies, runtime permissions, component protection, intent validation
- (~150-180 cuvinte, 1 paragraf compact)

**4.4 Vulnerabilități Criptografice**
- **Definiție:** Weak crypto, cert validation flaws, poor key management, SSL/TLS bugs
- **Manifestare:** MITM attacks, credential theft, insecure data storage
- **Soluții:** TEE/Keystore, cert pinning, TLS 1.3+, hardware-backed keys
- (~150-180 cuvinte, 1 paragraf compact)

**4.5 Vulnerabilități de Information Disclosure**
- **Definiție:** Memory leaks, side-channels, unintended data exposure, tracking APIs
- **Manifestare:** SQLite world-readable (pre-Android 4.4), Android ID leakage, sensor tracking
- **Soluții:** FBE, Scoped Storage, Privacy Dashboard, permission auto-reset
- (~150-180 cuvinte, 1 paragraf compact)

#### PARTEA II: Vectori de Atac

**4.6 Malware și Aplicații Malițioase**
- **Definiție:** Software malițios exploatând vulnerabilități 4.1-4.5 (troieni, spyware, ransomware)
- **Manifestare:** DroidDream (2011), GingerMaster (2011), Masque Attack (2014)
- **Soluții:** Google Play Protect, app sandboxing, runtime permissions, user education
- (~150-180 cuvinte, 1 paragraf compact)

**4.7 Riscuri Root/Jailbreak și ROM-uri Terțe**
- **Definiție:** Bypass intenționat protecții Android (UID 0, firmware modificat)
- **Manifestare:** Pre-rooted ROMs cu backdoors, banking apps blocked, SELinux disabled
- **Soluții:** Play Integrity API, Verified Boot warnings, user awareness (security vs customization)
- (~150-180 cuvinte, 1 paragraf compact)

**Total Cap 4:** ~1,050-1,260 cuvinte = 1.8-2.1 pag (COMPACT, respectă limitele)

---

### 📄 Pagini 6-8 - Cap 5: STUDII DE CAZ [2-2.5 pag]

⭐⭐⭐ **CEL MAI DETALIAT - FOCUS MAXIM**

**🔴 FEEDBACK PROFESOR:** Format lanț pentru fiecare caz: Vulnerabilitatea → Definirea atacului → Acțiunile → Efectele → Soluțiile

**Obiectiv:** Analiză tehnică profundă structurată ca un lanț logic

#### 5.1 Stagefright (2015) - Atac Media [~1-1.2 pag]

**5.1.1 Vulnerabilitatea** (1 paragraf, ~120 cuvinte):
- **Vulnerabilitatea tehnică:** Integer overflow în libstagefright (biblioteca C++ pentru procesare multimedia)
- **Localizare:** Procesarea fișierelor MP4/MKV/WebM în Android Media Server
- **Versiuni afectate:** Android 2.2 (Froyo) până la 5.1.1 (Lollipop)
- **Descoperire:** Joshua Drake (Zimperium), iulie 2015, prezentat la Black Hat USA
- **Cauza tehnică:** Lipsă validare bounds checking în parsing-ul metadata video

**5.1.2 Definirea Atacului** (1 paragraf, ~100 cuvinte):
- **Tipul atacului:** Remote Code Execution (RCE) fără interacțiune utilizator
- **Vectorul de atac:** MMS crafted cu fișier media malițios / pagini web / email attachments
- **Complexitate:** Medie-ridicată (necesită crafting specific al payload-ului)
- **Privilege-uri necesare:** Niciuna pentru aplicație, exploatare se face în contextul Media Server

**5.1.3 Acțiunile (Desfășurarea Atacului)** (1-2 paragrafe, ~150 cuvinte):
- **Pasul 1:** Trimitere MMS cu fișier media crafted sau acces la media malițioasă
- **Pasul 2:** Android Media Server procesează automat fișierul în background (fără interacțiune utilizator)
- **Pasul 3:** Integer overflow trigger în libstagefright → buffer overflow
- **Pasul 4:** Executare cod arbitrar în contextul Media Server (UID: media)
- **Pasul 5:** Privilege escalation către system/root prin vulnerabilități suplimentare
- **Pasul 6:** Control complet dispozitiv (citire date, instalare malware, interceptare comunicații)
- **Timeline:** Atacul poate fi executat în < 1 minut de la primirea MMS-ului

**5.1.4 Efectele (Impactul)** (1 paragraf, ~120 cuvinte):
- **950 milioane dispozitive vulnerabile** (95% din Android phones în 2015)
- **Stagefright 2.0:** ~1 miliard dispozitive afectate (variante ulterioare)
- **Acces complet:** Cameră, microfon, GPS, contacte, mesaje, apeluri
- **Exfiltrare date:** Date personale, corporate, financiare
- **Instalare malware persistent:** Rootkit-uri, spyware, ransomware
- **Atacuri țintite:** Jurnaliști, activiști, oficiali guvernamentali
- **Vector simplu:** Necesită doar numărul de telefon al victimei

**5.1.5 Soluțiile (Patch-uri și Mitigări)** (1-2 paragrafe, ~150 cuvinte):
- **Google Android Security Bulletin (august 2015):** Patch-uri pentru CVE-2015-1538/1539
- **Monthly Security Updates:** Google a implementat patch-uri lunare obligatorii
- **ASLR improvements:** Address Space Layout Randomization mai robust
- **Media Server sandboxing:** Izolare mai strictă a Media Server în Android 7.0+
- **Mediaserver refactoring:** Separarea componentelor în procese distincte (Android 8.0+)
- **Mitigări utilizator:** Dezactivare auto-retrieve MMS (temporar, incomplet)
- **Provocări:** Fragmentarea ecosistemului → multe dispozitive niciodată patch-uite
- **Lecție:** Monthly security updates devin standard industrie după Stagefright

**Total Stagefright:** ~640 cuvinte = 1.1-1.2 pag

---

#### 5.2 QuadRooter (2016) - Vulnerabilități în Drivers [~1-1.2 pag]

**5.2.1 Vulnerabilitatea** (1-2 paragrafe, ~150 cuvinte):
- **Vulnerabilitatea tehnică:** 4 CVE-uri în drivere proprietare Qualcomm
  - **CVE-2016-2503/2504:** Use-after-free în KGSL (GPU driver)
  - **CVE-2016-2059:** IPC router kernel module validation flaw
  - **CVE-2016-5340:** Ashmem pointer validation bug
- **Localizare:** Kernel-level drivers pentru Qualcomm Snapdragon
- **Versiuni afectate:** Dispozitive cu chipset-uri Qualcomm (Snapdragon 800/805/808/810/820)
- **Descoperire:** Adam Donenfeld (Check Point Research), prezentat DEF CON 24, august 2016
- **Cauza tehnică:** Lipsă validare în drivere proprietare, race conditions, memory corruption

**5.2.2 Definirea Atacului** (1 paragraf, ~100 cuvinte):
- **Tipul atacului:** Local Privilege Escalation (LPE) la root
- **Vectorul de atac:** Aplicație malițioasă **fără permisiuni speciale**
- **Complexitate:** Medie (exploit-uri disponibile public după disclosure)
- **Privilege-uri necesare:** Niciuna (aplicație normală fără permisiuni ridicate)
- **Stealth:** Aplicația nu ridică suspiciuni la instalare (zero permissions requested)

**5.2.3 Acțiunile (Desfășurarea Atacului)** (1-2 paragrafe, ~150 cuvinte):
- **Pasul 1:** Utilizator instalează aplicație aparent benignă (joc, utility, etc.)
- **Pasul 2:** Aplicația exploatează una dintre cele 4 vulnerabilități kernel
- **Pasul 3:** Trigger race condition sau memory corruption în driver-ul Qualcomm
- **Pasul 4:** Escaladare privilegii la root (UID 0)
- **Pasul 5:** **Bypass complet SELinux** prin execuție cod kernel
- **Pasul 6:** Dezactivare protecții: Play Integrity, Verified Boot, dm-verity
- **Pasul 7:** Persistență prin modificare /system (rootkit persistent)
- **Timeline:** Rooting complet în < 30 secunde după lansarea aplicației

**5.2.4 Efectele (Impactul)** (1 paragraf, ~120 cuvinte):
- **900 milioane dispozitive vulnerabile** (toate cu Qualcomm chipset)
- **Dispozitive afectate:** Nexus 5/5X/6/6P/7, Samsung Galaxy S6/S7, LG G4/G5, majoritatea flagship-urilor 2015-2016
- **Control complet:** Root privileges persistent, bypass toate protecțiile Android
- **Compromise corporate:** Acces la date enterprise (MDM bypass, corporate email)
- **Financial fraud:** Banking apps compromise, 2FA bypass, payment systems
- **Spionaj:** Instalare spyware invizibil, keyloggers, screen recording
- **Demonstrație:** SELinux și kernel protections nu sunt suficiente singure

**5.2.5 Soluțiile (Patch-uri și Mitigări)** (1-2 paragrafe, ~150 cuvinte):
- **Qualcomm patches:** Dezvoltate aprilie-iulie 2016, distribuite către OEM-uri
- **Google Android Security Bulletin (august-septembrie 2016):** Integrare patch-uri
- **Kernel hardening:** Control Flow Integrity (CFI), Stack canaries improvement
- **Driver security review:** Qualcomm a implementat code review mai strict pentru drivere
- **SELinux policy updates:** Restricții suplimentare pentru driver access
- **Play Protect enhancement:** Detecție comportament suspicious kernel-level
- **Mitigări utilizator:** Instalare doar din Google Play, evitare sideloading APK-uri
- **Provocări:** Update fragmentation → multe dispozitive niciodată patch-uite
- **Lecție:** Third-party vendor code (Qualcomm) poate compromite toată securitatea Android

**Total QuadRooter:** ~670 cuvinte = 1.1-1.2 pag

**Total Cap 5:** ~1,310 cuvinte = 2.2-2.4 pag

---

### ❌ Cap 6: Măsuri de Protecție - ELIMINAT COMPLET

**🔴 FEEDBACK PROFESOR:** Capitolul de măsuri generale este eliminat

**Motivație:**
- Soluțiile specifice sunt integrate în Cap 4 (per vulnerabilitate: 4.1-4.5)
- Soluțiile pentru studii de caz sunt în Cap 5 (5.1.5 Stagefright + 5.2.5 QuadRooter)
- Evităm redundanța și păstrăm focus pe analiza vulnerabilităților + soluții contextuale

---

### 📄 Pagini 8-9 - Cap 6: Concluzii + Bibliografie [1-1.5 pag]

**🔴 FEEDBACK PROFESOR:** Concluzii = sinteză + starea actuală a sistemului + atacuri care încă se pot face

#### 6.1 Sinteză a Observațiilor (1 paragraf, ~150 cuvinte)
- **Evoluția modelului de securitate Android:**
  - De la basic sandboxing (2007) la arhitectură multi-layer (2024)
  - SELinux, Verified Boot, FBE, TEE, Play Integrity
- **Lecții din vulnerabilități:**
  - Stagefright: fragmentarea = Achilles' heel
  - QuadRooter: vendor code = lanțul slab
  - Pattern: patch-uri există, dar distribuiton e problema
- **Provocări permanente:**
  - Fragmentarea ecosistemului (OEM-uri, carriers)
  - Tensiunea open-source vs securitate
  - Third-party dependencies (Qualcomm, MediaTek)

#### 6.2 Starea Actuală a Securității Android (2024-2025) (2 paragrafe, ~200 cuvinte)
**Progrese recente:**
- **Project Mainline (2019+):** Core components updatable prin Play Store → bypass OEM delays
- **Scoped Storage (Android 10+):** Limitare acces filesystem
- **Privacy Dashboard (Android 12+):** Transparență acces la cameră/microfon/locație
- **Permission auto-reset:** Revocă permisiuni apps nefolosite
- **Monthly security bulletins:** Proces matur de patch management
- **Play Integrity API (2023-2024):** Hardware attestation pentru banking/payment apps

**Limitări actuale:**
- **Update fragmentation persistă:** Dispozitive budget și mid-range rămân vulnerabile
- **Vendor security posture variabil:** Qualcomm, Samsung, Xiaomi cu responsiveness diferit
- **Custom ROM ecosystem:** Tensiune între enthusiasts și security requirements
- **Zero-day market:** APT groups și spyware vendors (NSO Pegasus, Quadream)

#### 6.3 Atacuri și Vulnerabilități Actuale (2024-2025) (2 paragrafe, ~200 cuvinte)
**Ce atacuri încă se pot face:**
- **Zero-click exploits:** Mesaje MMS/RCS cu payload-uri sofisticate (evoluție Stagefright)
- **Kernel exploits:** Drivere GPU/Camera/Modem (Qualcomm, ARM Mali)
- **Supply chain attacks:** Pre-installed malware pe dispozitive budget (Triada, xHelper)
- **Phishing evolved:** WebView exploits, deepfake voice/video pentru social engineering
- **Spyware comercial:** Pegasus (NSO Group), Reign (QuaDream) - zero-click, kernel-level
- **Banking trojans:** Anatsa, SharkBot, Godfather - overlay attacks, accessibility abuse
- **Credential stuffing:** Password reuse exploitation, 2FA bypass techniques

**Vectori de atac persistenți:**
- **Sideloading APKs:** Utilizatori bypass Play Store protections
- **Malicious apps în Play Store:** Evaziune temporară a Play Protect
- **Physical access attacks:** Forensic tools (Cellebrite, GrayKey)
- **Network-based:** Man-in-the-middle pe WiFi public, DNS hijacking
- **Social engineering:** Rămâne cel mai eficient vector

**Tendințe emergente:**
- **AI-powered attacks:** Generare automată exploits, adaptive malware
- **Quantum computing threat:** Viitoare compromise a criptografiei actuale (RSA, ECC)

#### 6.4 Bibliografie
✅ **\printbibliography** (automatic LaTeX)
- Format compact, IEEE style
- Estimat: 0.3-0.5 pag

#### 6.5 Contribuția Autorilor ✅
✅ **OBLIGATORIU - Menținut pentru notare**
- Secțiune scurtă: cine a lucrat la ce
- (1 paragraf, ~50 cuvinte)

**Total Cap 6:** ~600 cuvinte + bibliografie = 1.2-1.5 pag

---

## 📊 Sumar Total Estimat (ACTUALIZAT conform feedback profesor)

| Capitol | Pagini | Cuvinte | Focus | Status |
|---------|--------|---------|-------|--------|
| 1. Introducere | 1 | ~450 | ✅ Complet | ✅ SCRIS |
| 2. Arhitectura Android | 1-1.5 | ~400 | Concis | ✅ SCRIS |
| 3. Modelul de Securitate | 2-2.5 | ~1,400 | ⭐⭐⭐ Maxim | ✅ SCRIS |
| 4. Vulnerabilități + Soluții | 1.5-2 | ~1,000 | ⭐⭐ Detaliat | 🔴 DE SCRIS |
| 5. Studii de Caz (lanț) | 2-2.5 | ~1,310 | ⭐⭐⭐ Maxim | 🔴 DE SCRIS |
| ~~6. Măsuri Protecție~~ | ❌ | ❌ | ELIMINAT | ❌ |
| 6. Concluzii + Bibliografie | 1.2-1.5 | ~600 + refs | Sinteză + Stare actuală | 🔴 DE SCRIS |
| **TOTAL** | **9-10** | **~5,160** | 🎯 Perfect | **3/6 complete** |

---

## ❌ Eliminări Complete

1. **Cap 6 - Măsuri de Protecție generale** → Integrate în Cap 4 (per vulnerabilitate) și Cap 5 (per studiu de caz)
2. **Appendix A - Exemplu Politică SELinux** (prea tehnic, consumă spațiu)
3. **Appendix B - Glosar de Termeni** (termenii explicați în text)

---

## 🎯 Priorități de Scriere (ACTUALIZAT conform feedback)

### ✅ Nivel 1 - COMPLETAT:
1. ✅ **Cap 1 - Introducere** (context + obiective)
2. ✅ **Cap 2 - Arhitectura Android** (fundație tehnică)
3. ✅ **Cap 3 - Modelul de Securitate** (sandboxing, SELinux, TEE, etc.)

### 🔴 Nivel 2 - SCRIE ACUM (core value):
4. ⭐⭐⭐ **Cap 5 - Studii de Caz** (format lanț: vulnerabilitate → atac → acțiuni → efecte → soluții)
   - 5.1 Stagefright (2015)
   - 5.2 QuadRooter (2016)

### 🔴 Nivel 3 - SCRIE URMĂTOARELE:
5. ⭐⭐ **Cap 4 - Vulnerabilități + Soluții** (definiție + manifestare + soluții per vulnerabilitate)
   - 4.1 Exploatarea Privilegiilor
   - 4.2 Vulnerabilități Kernel/Driver
   - 4.3 Malware
   - 4.4 Root/Custom ROM
   - 4.5 Privacy/Data Leaks

6. ⭐⭐ **Cap 6 - Concluzii** (sinteză + stare actuală 2024-2025 + atacuri curente)

---

## 📝 Note Stilistice

- **Ton academic formal** (română, stil licență Cristian)
- **Paragrafe scurte** (3-5 propoziții pentru două coloane)
- **Date concrete:** cifre, CVE-uri, versiuni Android specifice
- **Referințe bibliografice:** \cite{} pentru toate afirmațiile
- **Exemple tehnice:** code snippets unde e relevant
- **Note personale subtile:** Experiența cu rooting (introducere + concluzii)
- **Humor moderat:** 😤 Play Integrity banking frustration (contextual appropriate)

---

## 🔄 Workflow Recomandat (ACTUALIZAT conform feedback)

### ✅ Completat (deja scris):
1. ✅ Cap 1 - Introducere
2. ✅ Cap 2 - Arhitectura Android
3. ✅ Cap 3 - Modelul de Securitate

### 🔴 De scris (în ordine priorității):
4. **Cap 5 - Studii de Caz (format lanț)** - 3 ore
   - Stagefright: vulnerabilitate → atac → acțiuni → efecte → soluții
   - QuadRooter: vulnerabilitate → atac → acțiuni → efecte → soluții

5. **Cap 4 - Vulnerabilități + Soluții integrate** - 2.5 ore
   - Pentru fiecare vulnerabilitate: definiție + manifestare + soluții specifice

6. **Cap 6 - Concluzii (sinteză + stare actuală + atacuri curente)** - 1.5 ore
   - Sinteză observații
   - Starea actuală 2024-2025
   - Ce atacuri încă se pot face

7. **Review + ajustări + bibliografie** - 1 oră

**Timp total rămas estimat:** 8 ore scriere

---

## 📋 Checklist Final

- [x] Introducere (context + obiective)
- [x] Arhitectura Android (fundație tehnică)
- [x] Modelul de Securitate (mecanisme + extensii moderne)
- [ ] **Vulnerabilități + Soluții integrate** (definiție + manifestare + soluții per vulnerabilitate)
- [ ] **Studii de Caz format lanț** (vulnerabilitate → atac → acțiuni → efecte → soluții)
- [ ] **Concluzii actualizate** (sinteză + stare actuală + atacuri curente)
- [ ] Bibliografie completă
- [ ] Contribuția autorilor

---

**Ultima actualizare:** 10 noiembrie 2025
**Status:** Arhitectură restructurată conform feedback profesor - 50% completă, gata pentru scrierea capitolelor rămase
