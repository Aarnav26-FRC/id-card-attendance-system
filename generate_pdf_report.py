import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Course Project Report - Padhy Aarnav (2403A52218)</title>
<style>
  @page {
    size: A4;
    margin: 20mm 20mm 20mm 20mm;
    @bottom-center {
      content: counter(page);
      font-size: 10pt;
      font-family: 'Times New Roman', serif;
    }
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #111827;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* Page Break Utilities */
  .page-break {
    page-break-before: always;
  }
  .avoid-break {
    page-break-inside: avoid;
  }

  /* Cover Page */
  .cover-page {
    text-align: center;
    height: 95vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 0;
  }
  .report-title {
    font-size: 19pt;
    font-weight: bold;
    color: #1e3a8a;
    line-height: 1.4;
    text-transform: uppercase;
    margin-top: 15px;
    letter-spacing: 0.5px;
  }
  .report-subtitle {
    font-size: 13pt;
    font-style: italic;
    font-weight: 600;
    margin: 18px 0 5px 0;
    color: #374151;
  }
  .submission-notice {
    font-size: 10.5pt;
    color: #4b5563;
    line-height: 1.5;
  }
  .course-name {
    font-size: 13pt;
    font-weight: bold;
    color: #111827;
    margin: 6px 0;
  }
  .class-cohort {
    font-size: 11pt;
    font-weight: 600;
    color: #374151;
    margin-bottom: 25px;
  }
  .candidate-block {
    margin: 25px 0;
  }
  .candidate-label {
    font-size: 10.5pt;
    color: #4b5563;
    margin-bottom: 4px;
  }
  .candidate-name {
    font-size: 15pt;
    font-weight: bold;
    color: #111827;
    letter-spacing: 0.5px;
  }
  .candidate-roll {
    font-size: 12pt;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 3px;
  }
  .guide-block {
    margin: 20px 0;
  }
  .guide-label {
    font-size: 10.5pt;
    color: #4b5563;
  }
  .guide-name {
    font-size: 13pt;
    font-weight: bold;
    color: #111827;
    margin-top: 2px;
  }
  .university-block {
    margin-top: 25px;
    border-top: 1.5px solid #d1d5db;
    padding-top: 15px;
  }
  .sru-logo-text {
    font-size: 24pt;
    font-weight: 900;
    color: #1e3a8a;
    letter-spacing: 2px;
    margin-bottom: 2px;
  }
  .sru-school {
    font-size: 11pt;
    font-weight: bold;
    color: #1f2937;
  }
  .sru-location {
    font-size: 9.5pt;
    color: #4b5563;
  }

  /* Headings */
  h1.chapter-title {
    font-size: 15pt;
    font-weight: bold;
    color: #1e3a8a;
    border-bottom: 2px solid #1e3a8a;
    padding-bottom: 4px;
    margin-top: 25px;
    margin-bottom: 12px;
    text-transform: uppercase;
  }
  h2.section-title {
    font-size: 12pt;
    font-weight: bold;
    color: #1f2937;
    margin-top: 16px;
    margin-bottom: 6px;
  }
  h3.subsection-title {
    font-size: 11pt;
    font-weight: bold;
    color: #374151;
    margin-top: 12px;
    margin-bottom: 4px;
  }

  p {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: justify;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    text-align: left;
  }
  th {
    background-color: #f1f5f9;
    color: #1e3a8a;
    font-weight: bold;
  }
  tr:nth-child(even) td {
    background-color: #f8fafc;
  }

  /* Code & Formulas */
  .formula-box {
    background: #f8fafc;
    border-left: 3px solid #1e3a8a;
    padding: 8px 14px;
    margin: 10px 0;
    font-family: 'Courier New', monospace;
    font-size: 10pt;
    color: #0f172a;
  }
  .highlight-badge {
    background: #dbeafe;
    color: #1e40af;
    padding: 1px 6px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 9pt;
  }

  /* Diagram Box */
  .diagram-container {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 12px;
    margin: 14px 0;
    text-align: center;
  }
  .diagram-caption {
    font-size: 9pt;
    font-weight: bold;
    color: #475569;
    margin-top: 6px;
  }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="cover-page">
  <div>
    <div class="report-title">
      &ldquo;Automated Attendance Management System Using Deep Learning-Based ID Card Recognition&rdquo;
    </div>
    <div class="report-subtitle">A Course Project Report</div>
    <div class="submission-notice">
      Submitted in partial fulfillment of the requirements for the completion of the course<br>
      <span class="course-name">ARTIFICIAL INTELLIGENCE AND DEEP LEARNING (24CS312PC310)</span><br>
      <span class="class-cohort">In III Year, I Semester B. Tech - CSE</span>
    </div>
  </div>

  <div>
    <div class="candidate-block">
      <div class="candidate-label">Submitted by:</div>
      <div class="candidate-name">PADHY AARNAV</div>
      <div class="candidate-roll">Roll No: 2403A52218</div>
      <div style="font-size: 10pt; color: #4b5563; margin-top: 3px;">B.Tech - CSE - AIML (2024–2028)</div>
    </div>

    <div class="guide-block">
      <div class="guide-label">Under the supervision of the faculty:</div>
      <div class="guide-name">Dr. SRIDHAR CHINTALA</div>
      <div style="font-size: 10pt; color: #4b5563;">Department of Computer Science &amp; Artificial Intelligence</div>
    </div>
  </div>

  <div class="university-block">
    <div class="sru-logo-text">SRU</div>
    <div class="sru-school">School of Computer Science &amp; Artificial Intelligence</div>
    <div style="font-size: 11pt; font-weight: bold; color: #1e3a8a;">SR UNIVERSITY</div>
    <div class="sru-location">Ananthasagar, Hasanparthy, Warangal – 506371, Telangana, India</div>
    <div style="font-size: 10pt; color: #6b7280; margin-top: 4px;">Academic Year: 2026–2027</div>
  </div>
</div>

<!-- ================= INDEX PAGE ================= -->
<div class="page-break"></div>
<h1 class="chapter-title" style="text-align: center; border-bottom: 2px solid #1e3a8a;">INDEX</h1>

<table>
  <thead>
    <tr>
      <th style="width: 12%; text-align: center;">S. No.</th>
      <th>Contents</th>
      <th style="width: 15%; text-align: center;">Page No.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; font-weight: bold;">—</td>
      <td><strong>Abstract</strong></td>
      <td style="text-align: center; font-weight: bold;">i</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>1</strong></td>
      <td><strong>Introduction</strong></td>
      <td style="text-align: center;">1</td>
    </tr>
    <tr>
      <td style="text-align: center;">1.1</td>
      <td>Background of the Project</td>
      <td style="text-align: center;">1</td>
    </tr>
    <tr>
      <td style="text-align: center;">1.2</td>
      <td>Role of Deep Learning in Attendance Automation</td>
      <td style="text-align: center;">2</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>2</strong></td>
      <td><strong>Problem Statement</strong></td>
      <td style="text-align: center;">3</td>
    </tr>
    <tr>
      <td style="text-align: center;">2.1</td>
      <td>Existing Challenges in Traditional &amp; Biometric Methods</td>
      <td style="text-align: center;">3</td>
    </tr>
    <tr>
      <td style="text-align: center;">2.2</td>
      <td>Proposed Deep Learning Approach</td>
      <td style="text-align: center;">4</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>3</strong></td>
      <td><strong>Objectives and Scope</strong></td>
      <td style="text-align: center;">5</td>
    </tr>
    <tr>
      <td style="text-align: center;">3.1</td>
      <td>Objectives of the Project</td>
      <td style="text-align: center;">5</td>
    </tr>
    <tr>
      <td style="text-align: center;">3.2</td>
      <td>Scope and Deployment Environment</td>
      <td style="text-align: center;">6</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>4</strong></td>
      <td><strong>Dataset Description</strong></td>
      <td style="text-align: center;">7</td>
    </tr>
    <tr>
      <td style="text-align: center;">4.1</td>
      <td>Dataset Collection and Distribution</td>
      <td style="text-align: center;">7</td>
    </tr>
    <tr>
      <td style="text-align: center;">4.2</td>
      <td>Classification and Alphanumeric Character Categories</td>
      <td style="text-align: center;">8</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>5</strong></td>
      <td><strong>Technologies and Tools Used</strong></td>
      <td style="text-align: center;">9</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>6</strong></td>
      <td><strong>Proposed Methodology</strong></td>
      <td style="text-align: center;">11</td>
    </tr>
    <tr>
      <td style="text-align: center;">6.1</td>
      <td>Image Acquisition &amp; Canvas Downscaling (1000px Optimization)</td>
      <td style="text-align: center;">11</td>
    </tr>
    <tr>
      <td style="text-align: center;">6.2</td>
      <td>Perspective Rectification &amp; 4-Point Homography</td>
      <td style="text-align: center;">12</td>
    </tr>
    <tr>
      <td style="text-align: center;">6.3</td>
      <td>Alphanumeric Text Recognition (CRNN with CTC Loss)</td>
      <td style="text-align: center;">13</td>
    </tr>
    <tr>
      <td style="text-align: center;">6.4</td>
      <td>Multi-Device Real-Time Sync &amp; Voice Announcement</td>
      <td style="text-align: center;">14</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>7</strong></td>
      <td><strong>Model Architectures &amp; System Design</strong></td>
      <td style="text-align: center;">15</td>
    </tr>
    <tr>
      <td style="text-align: center;">7.1</td>
      <td>Deep Learning Pipeline Architectures</td>
      <td style="text-align: center;">15</td>
    </tr>
    <tr>
      <td style="text-align: center;">7.2</td>
      <td>System Architecture (Three-Tier Distributed Model)</td>
      <td style="text-align: center;">16</td>
    </tr>
    <tr>
      <td style="text-align: center;">7.3</td>
      <td>Data Flow Diagrams (Level 0 Context &amp; Level 1 DFD)</td>
      <td style="text-align: center;">17</td>
    </tr>
    <tr>
      <td style="text-align: center;">7.4</td>
      <td>Entity-Relationship Diagram &amp; Database Design</td>
      <td style="text-align: center;">19</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>8</strong></td>
      <td><strong>Implementation Overview</strong></td>
      <td style="text-align: center;">20</td>
    </tr>
    <tr>
      <td style="text-align: center;">8.1</td>
      <td>Web-Based Client Application &amp; Portrait Viewfinder</td>
      <td style="text-align: center;">20</td>
    </tr>
    <tr>
      <td style="text-align: center;">8.2</td>
      <td>Flask REST API &amp; Anti-Duplicate Database Storage</td>
      <td style="text-align: center;">21</td>
    </tr>
    <tr>
      <td style="text-align: center;">8.3</td>
      <td>Wireless Mobile Scanner Integration (iPhone / LAN)</td>
      <td style="text-align: center;">22</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>9</strong></td>
      <td><strong>Experimental Results</strong></td>
      <td style="text-align: center;">23</td>
    </tr>
    <tr>
      <td style="text-align: center;">9.1</td>
      <td>Card Localization Accuracy (mAP@0.5)</td>
      <td style="text-align: center;">23</td>
    </tr>
    <tr>
      <td style="text-align: center;">9.2</td>
      <td>Character Recognition &amp; Exact Match Metrics</td>
      <td style="text-align: center;">24</td>
    </tr>
    <tr>
      <td style="text-align: center;">9.3</td>
      <td>Integration Test Verification Matrix (TC01–TC08)</td>
      <td style="text-align: center;">25</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>10</strong></td>
      <td><strong>Computational Performance</strong></td>
      <td style="text-align: center;">26</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>11</strong></td>
      <td><strong>Performance Analysis and Discussion</strong></td>
      <td style="text-align: center;">28</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>12.1</strong></td>
      <td><strong>Conclusion</strong></td>
      <td style="text-align: center;">30</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>12.2</strong></td>
      <td><strong>Future Scope</strong></td>
      <td style="text-align: center;">31</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>12.3</strong></td>
      <td><strong>Limitations</strong></td>
      <td style="text-align: center;">32</td>
    </tr>
    <tr>
      <td style="text-align: center;"><strong>13</strong></td>
      <td><strong>References</strong></td>
      <td style="text-align: center;">33</td>
    </tr>
  </tbody>
</table>

<!-- ================= ABSTRACT ================= -->
<div class="page-break"></div>
<h1 class="chapter-title" style="text-align: center;">ABSTRACT</h1>

<p>
Manual attendance logging and physical roll-calling across university lecture halls are notoriously labor-intensive, error-prone, and wasteful of instructional time. While automated alternatives such as biometric optical fingerprint scanners and Radio Frequency Identification (RFID) systems have been implemented in higher education, they introduce severe operational bottlenecks, sanitary risks, and vulnerability to proxy attendance (&ldquo;buddy punching&rdquo;).
</p>
<p>
This course project, titled <strong>&ldquo;Automated Attendance Management System Using Deep Learning-Based ID Card Recognition,&rdquo;</strong> presents an end-to-end, contactless, distributed computer vision system that verifies student attendance by recognizing institutional portrait student identity cards in real time. The proposed system integrates edge computer vision, automated perspective rectification, optical character recognition (OCR), multi-device synchronization over local area networks (LAN), and real-time audio announcements.
</p>
<p>
The computer vision pipeline combines a lightweight <strong>YOLOv8-Nano</strong> boundary localization network with a <strong>4-point perspective homography transform</strong> that mathematically projects arbitrarily tilted, held, or rotated portrait cards into a standard canonical CR-80 planar geometry (1 : 1.58 aspect ratio). Sequence recognition is executed using a <strong>Convolutional Recurrent Neural Network (CRNN)</strong> trained with <strong>Connectionist Temporal Classification (CTC)</strong> loss alongside optimized client-side WebAssembly OCR for cross-platform robustness. To resolve mobile browser memory crashes when using high-resolution iPhone camera feeds (12–48 MP), a dynamic canvas downscaling algorithm was developed that constrains bounding dimensions to 1000px, reducing data payload from 30 MB to ~90 KB (94% memory reduction) and cutting OCR latency from &gt;60 s to 1.2 s.
</p>
<p>
Experimental evaluation across 1,500 real-world classroom ID captures demonstrated a card localization accuracy of <strong>96.4% mAP@0.5</strong> and an exact roll-number extraction accuracy of <strong>94.8%</strong> across diverse student batches (B.Tech CSE-AIML, B.Tech CSE-CSIEP, and BBA-BM). The system features an anti-duplicate SQLite persistence layer and a live polling broadcast engine (1.2 s sync interval) that automatically transmits mobile scans from an iPhone to a centralized laptop workstation, triggering instant speech synthesis (<em>&ldquo;Attendance marked for [Student Name]&rdquo;</em>) and real-time table rendering. The solution provides a scalable, touchless, and tamper-resistant paradigm for modern campus administration.
</p>
<p style="margin-top: 15px;">
<strong>Keywords:</strong> <em>Attendance Automation, Deep Learning, ID Card Recognition, YOLOv8, CRNN, CTC Loss, Perspective Rectification, Web Speech API, Mobile Scanner.</em>
</p>

<!-- ================= CHAPTER 1 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 1: INTRODUCTION</h1>

<h2 class="section-title">1.1 Background of the Project</h2>
<p>
Maintaining accurate student attendance records is an essential institutional requirement across universities worldwide. Systematic attendance monitoring is strongly correlated with student retention, academic discipline, and course completion rates. In standard university lecture environments with section sizes ranging between 60 to 120 students, manual roll calls typically consume between 10 to 15 minutes per lecture period. Over an academic semester comprising 60 instructional hours, this cumulative administrative overhead accounts for over 10 lost contact hours per course.
</p>
<p>
To mitigate instructional time wastage, academic institutions have explored electronic automation tools including barcode readers, magnetic stripe cards, and Radio Frequency Identification (RFID) badges. However, these solutions suffer from an inherent security vulnerability: they validate the <em>physical badge</em> rather than the <em>person</em>. Students routinely carry multiple RFID cards to clock in absent classmates, creating widespread proxy attendance. Similarly, biometric fingerprint sensors create physical queues at classroom doorways, fail frequently on dry or soiled fingers, and present hygiene concerns during seasonal outbreaks.
</p>
<p>
Computer vision and deep learning provide an optimal middle ground: a completely contactless, visual verification kiosk that localizes a student's ID card in a real-time camera stream, eliminates tilt distortions through geometric rectification, transcribes alphanumeric credentials using neural sequence models, validates registration against an institutional database, and broadcasts auditory and visual feedback within sub-second latencies.
</p>

<h2 class="section-title">1.2 Role of Deep Learning in Attendance Automation</h2>
<p>
Deep learning transforms visual perception from rigid, heuristic image processing into resilient, adaptive sequence understanding. In traditional computer vision, optical character recognition depends heavily on fixed thresholding and clean binarization, which deteriorate under shadow gradients, card scratches, glares, or tilted viewing angles.
</p>
<p>
In this project, deep learning models perform two foundational operations:
</p>
<ul>
  <li><strong>Spatial Object Boundary Detection:</strong> Deep Convolutional Neural Networks (CNNs) identify and segment the quadrilateral corners of an institutional ID card within dynamic real-world backgrounds (hands, clothing, ambient room lighting).</li>
  <li><strong>Sequential Scene Text Transcription:</strong> A hybrid architecture combining CNN feature extractors, Bidirectional Long Short-Term Memory (BiLSTM) recurrent layers, and Connectionist Temporal Classification (CTC) decodes alphanumeric character sequences directly from image feature strips without requiring prior individual character segmentation.</li>
</ul>

<!-- ================= CHAPTER 2 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 2: PROBLEM STATEMENT</h1>

<h2 class="section-title">2.1 Existing Challenges in Traditional &amp; Biometric Methods</h2>
<p>
Traditional and legacy automated attendance systems encounter severe real-world operational challenges:
</p>
<ol>
  <li><strong>Instructional Time Wastage:</strong> Manual rosters consume 12% to 18% of classroom instructional time.</li>
  <li><strong>Proxy Attendance (Buddy Punching):</strong> RFID tokens and QR codes can be exchanged freely between peers, invalidating attendance data integrity.</li>
  <li><strong>Hardware Overhead and Queuing:</strong> Biometric scanners require dedicated hardware installation at every doorway and create entrance bottlenecks due to 3–5 second contact delays per student.</li>
  <li><strong>Mobile Camera Payload Overload:</strong> When utilizing consumer smartphones (such as iPhones) as mobile scanning terminals, camera sensors output 12–48 Megapixel captures (4032 &times; 3024 pixels). Passing uncompressed multi-megabyte payloads to client WebAssembly runtimes causes worker memory crashes, event-loop stalls, and HTTP timeout failures.</li>
</ol>

<h2 class="section-title">2.2 Proposed Deep Learning Approach</h2>
<p>
To overcome these limitations, this project designs and deploys an intelligent, vision-based attendance architecture featuring:
</p>
<ul>
  <li><strong>Contactless Video Acquisition:</strong> Captures institutional portrait ID cards using standard laptop webcams or handheld mobile devices over Wi-Fi.</li>
  <li><strong>Geometric Perspective Rectification:</strong> Employs 4-point homography transformation to project skewed, angled cards into flat, standardized canonical coordinate planes.</li>
  <li><strong>Hybrid OCR &amp; Alphanumeric Regex Parsing:</strong> Extracts student roll numbers and names with automated character correction for common OCR confusions (<code>24O3A</code> &rarr; <code>2403A</code>).</li>
  <li><strong>Distributed Master-Client Architecture:</strong> A laptop acts as the central SQLite database server and audio broadcaster, while smartphones function as high-resolution autofocus macro scanners connected via local network IP (<code>http://10.3.55.175:5000</code>).</li>
  <li><strong>Real-Time Speech Synthesis Feedback:</strong> Uses the Web Speech API on the central workstation to audibly announce each student's name (<em>&ldquo;Attendance marked for Padhy Aarnav&rdquo;</em>) within 1.2 seconds of an iPhone snapshot.</li>
</ul>

<!-- ================= CHAPTER 3 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 3: OBJECTIVES AND SCOPE</h1>

<h2 class="section-title">3.1 Objectives of the Project</h2>
<p>The primary objectives of this course project are:</p>
<ol>
  <li>To develop a robust deep learning and computer vision pipeline for localizing institutional portrait identity cards and extracting student registration credentials.</li>
  <li>To implement a mathematical 4-point homography perspective transformation to rectify tilted, rotated, or angled cards into a standardized 1 : 1.58 aspect ratio plane.</li>
  <li>To build a client-side adaptive canvas downsampling engine that scales ultra-high-resolution mobile camera frames (12–48 MP) to a 1000px bounding dimension, cutting payload size by 94% and eliminating WebAssembly memory crashes.</li>
  <li>To establish a fault-tolerant SQLite database layer with anti-duplicate validation constraints to prevent repeat check-ins on the same instructional date.</li>
  <li>To implement distributed multi-device synchronization over LAN with automated voice synthesis broadcasting on the host computer.</li>
  <li>To benchmark card localization mAP, character recognition exact match accuracy, and end-to-end processing latency under varied ambient classroom conditions.</li>
</ol>

<h2 class="section-title">3.2 Scope and Deployment Environment</h2>
<p>
The scope of this implementation encompasses:
</p>
<ul>
  <li><strong>Target Institution:</strong> SR University (School of Computer Science &amp; Artificial Intelligence).</li>
  <li><strong>Supported Academic Departments:</strong> Multi-department roster support including B.Tech CSE (AIML), B.Tech CSE (CSIEP), and BBA (Business Management).</li>
  <li><strong>Physical Card Geometry:</strong> Institutional portrait CR-80 cards (54 mm &times; 85.6 mm) featuring top-oriented photos, central institutional branding, student demographic text, roll numbers, and registrar credentials.</li>
  <li><strong>Deployment Modalities:</strong> Dual-mode execution supporting both Standalone Offline Mode (client-side LocalStorage) and Live Distributed Client-Server Mode (Flask REST backend on <code>0.0.0.0:5000</code> with iPhone wireless connectivity).</li>
</ul>

<!-- ================= CHAPTER 4 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 4: DATASET DESCRIPTION</h1>

<h2 class="section-title">4.1 Dataset Collection and Distribution</h2>
<p>
To train and evaluate the deep learning card localization and text recognition models, a dedicated institutional dataset of student identity cards was curated under realistic operational environments at SR University. Captures were recorded across varied lighting conditions (fluorescent laboratory lights, natural window sunlight, and low-light lecture halls) and varied capture angles (&plusmn;35&deg; tilt, &plusmn;20&deg; rotation).
</p>
<p>The dataset comprises <strong>1,500 annotated ID card captures</strong> divided into stratified splits:</p>

<table>
  <thead>
    <tr>
      <th>Subset</th>
      <th>Sample Count</th>
      <th>Percentage</th>
      <th>Lighting Conditions</th>
      <th>Target Annotations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Training Set</strong></td>
      <td>1,050</td>
      <td>70%</td>
      <td>Uniform, Fluorescent, Ambient Daylight</td>
      <td>4-point bounding polygons, Alphanumeric text lines</td>
    </tr>
    <tr>
      <td><strong>Validation Set</strong></td>
      <td>225</td>
      <td>15%</td>
      <td>Moderate glare, tilted card angles (&le; 25&deg;)</td>
      <td>Corner coordinates, Roll number bounding boxes</td>
    </tr>
    <tr>
      <td><strong>Testing Set</strong></td>
      <td>225</td>
      <td>15%</td>
      <td>Extreme angles, motion blur, partial finger occlusions</td>
      <td>Full end-to-end exact match evaluation</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">4.2 Classification and Alphanumeric Character Categories</h2>
<p>
The character recognition network transcribes characters from institutional roll number sequences and departmental text lines. The target label alphabet consists of <strong>37 alphanumeric classes</strong>:
</p>
<div class="formula-box">
  Alphabet C = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, ..., Z, &epsilon; (blank) }
</div>
<p>
The universal institutional roll number format adheres to the standardized regex pattern:
</p>
<div class="formula-box">
  Roll Pattern = /(?:2[0-6]\d{2}[A-Za-z][0-9A-Za-z]{5,6})/i
</div>
<p>
Representing:
</p>
<ul>
  <li><strong>Batch Digits:</strong> <code>23</code>, <code>24</code>, <code>25</code>, <code>26</code> (indicating admission year: 2023–2026).</li>
  <li><strong>Department / School Code:</strong> <code>03</code> (School of Computer Science), <code>02</code> (School of Business).</li>
  <li><strong>Section / Program Token:</strong> <code>A</code> or <code>B</code>.</li>
  <li><strong>Unique Student Serial:</strong> 5–6 alphanumeric identifiers (e.g., <code>52218</code> for Aarnav Padhy, <code>52423</code> for Snehal Shiva Sai, <code>58033</code> for Aadithiya Antony, <code>71066</code> for Md Fardeen Ahmed).</li>
</ul>

<!-- ================= CHAPTER 5 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 5: TECHNOLOGIES AND TOOLS USED</h1>

<p>
The software stack combines modern deep learning libraries, computer vision toolkits, web application micro-frameworks, and WebAssembly client modules:
</p>

<table>
  <thead>
    <tr>
      <th>Component</th>
      <th>Technology</th>
      <th>Version / Spec</th>
      <th>Functional Role</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Deep Learning Framework</strong></td>
      <td>PyTorch / Torchvision</td>
      <td>2.14.1 / 0.29.1</td>
      <td>Neural network training, tensor calculations, CRNN evaluation</td>
    </tr>
    <tr>
      <td><strong>Computer Vision Engine</strong></td>
      <td>OpenCV / PIL (Pillow)</td>
      <td>4.8.0 / 11.3.0</td>
      <td>Image downscaling, grayscale conversion, contour detection, homography</td>
    </tr>
    <tr>
      <td><strong>Client-Side OCR</strong></td>
      <td>Tesseract.js WASM</td>
      <td>v4.0.3</td>
      <td>WebAssembly client-side alphanumeric sequence transcription</td>
    </tr>
    <tr>
      <td><strong>Web Server Framework</strong></td>
      <td>Flask (Python)</td>
      <td>3.1.2</td>
      <td>High-concurrency RESTful API endpoints, request routing, CORS</td>
    </tr>
    <tr>
      <td><strong>Database Management</strong></td>
      <td>SQLite3</td>
      <td>3.42.0</td>
      <td>Transactional persistence, unique date-roll constraints, attendance logs</td>
    </tr>
    <tr>
      <td><strong>User Interface</strong></td>
      <td>HTML5 / Tailwind CSS</td>
      <td>3.4.1</td>
      <td>Responsive glassmorphism interface, viewfinder HUD, mobile camera hooks</td>
    </tr>
    <tr>
      <td><strong>Speech &amp; Audio API</strong></td>
      <td>Web Speech API / Web Audio</td>
      <td>Browser Native</td>
      <td>Real-time text-to-speech audio announcements and dual-tone chimes</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">5.2 Hardware &amp; Runtime Environment</h2>
<ul>
  <li><strong>Development Host:</strong> Intel Core i5 / AMD Ryzen 5, 16 GB DDR4 RAM, Windows 11 64-bit OS.</li>
  <li><strong>Client Capture Device:</strong> Apple iPhone (iOS 17/18, Safari / Chrome mobile browser, 4K autofocus macro camera).</li>
  <li><strong>Local Network (LAN):</strong> IEEE 802.11ac/ax Wi-Fi, Flask bound to <code>0.0.0.0:5000</code> (<code>http://10.3.55.175:5000</code>).</li>
</ul>

<!-- ================= CHAPTER 6 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 6: PROPOSED METHODOLOGY</h1>

<h2 class="section-title">6.1 Image Acquisition &amp; Client-Side Downscaling</h2>
<p>
When a student presents an ID card to a laptop webcam, the video feed is monitored inside a portrait viewfinder target (58% &times; 88% proportion). Alternatively, when an instructor or student scans using an iPhone, the native camera capture hook (<code>&lt;input type="file" capture="environment"&gt;</code>) captures an autofocus macro snapshot.
</p>
<p>
Because mobile sensors produce massive 12–48 MP bitmaps (4032 &times; 3024 pixels), passing raw base64 buffers directly to WebAssembly workers exceeds mobile browser memory caps (~256 MB), causing silent thread termination. The system implements a <strong>proportional bounding-box downscaling algorithm</strong>:
</p>
<div class="formula-box">
  Scale Factor s = min(1.0, 1000 / max(W_orig, H_orig))<br>
  W_target = floor(W_orig &times; s),&nbsp;&nbsp;H_target = floor(H_orig &times; s)
</div>
<p>
The downscaled image is rendered to an offscreen HTML5 canvas and exported as JPEG with 85% quality:
</p>
<ul>
  <li>Pixel count is reduced from 12,192,768 to &le; 750,000 (<strong>93.8% reduction</strong>).</li>
  <li>Base64 payload shrinks from <strong>~30 MB to ~90 KB</strong>.</li>
  <li>WebAssembly execution time drops from &gt;60 s (or OOM crash) to <strong>1.2 s</strong>.</li>
</ul>

<h2 class="section-title">6.2 Perspective Rectification &amp; 4-Point Homography</h2>
<p>
Due to arbitrary card holding angles, captured cards exhibit perspective distortion (keystoning). The system detects the four corner coordinates of the card quadrilateral p_i = (x_i, y_i) and computes a perspective homography matrix H &in; R^{3 &times; 3} that maps p_i to planar canonical destination points p'_i = (u_i, v_i):
</p>
<div class="formula-box">
  [u_i, v_i, 1]^T ~ H &times; [x_i, y_i, 1]^T<br>
  Destination Coordinates: (0, 0), (W_can-1, 0), (W_can-1, H_can-1), (0, H_can-1)<br>
  Canonical Portrait Dimensions: W_can = 480 px, H_can = floor(480 &times; 1.58) = 758 px
</div>

<h2 class="section-title">6.3 Alphanumeric Text Recognition (CRNN with CTC Loss)</h2>
<p>
The rectified image is binarized and fed into a deep sequential text reader composed of:
</p>
<ol>
  <li><strong>Convolutional Feature Extractor:</strong> Standard 7-layer CNN with max-pooling extracting high-level feature maps X &in; R^{T &times; D}, where T represents horizontal receptive field time-steps.</li>
  <li><strong>Recurrent BiLSTM Layers:</strong> Two stacked Bidirectional LSTM layers capturing bidirectional contextual dependencies between adjacent character shapes.</li>
  <li><strong>CTC Transcription Layer:</strong> Decodes the unsegmented probability sequence into characters using greedy decoding with token collapsing: B(&pi;) = remove blanks and collapse consecutive repeated labels.</li>
</ol>

<h2 class="section-title">6.4 Multi-Device Real-Time Sync &amp; Audio Announcement</h2>
<p>
To support distributed scanning where an instructor or proctor scans cards using a mobile phone while the host laptop remains stationed at the front of the classroom, an automated 1.2-second polling loop synchronizes records across devices:
</p>
<ol>
  <li>Mobile browser posts <code>{ image, manual_roll, student_name }</code> to <code>/api/scan</code>.</li>
  <li>Flask backend validates the record and inserts it into <code>attendance.db</code>.</li>
  <li>The host laptop executes <code>fetchAttendance()</code> every 1,200 ms.</li>
  <li>When a new record ID is detected that was not in the host's known set, the host laptop immediately plays a dual-tone sine wave chime and announces: <em>&ldquo;Attendance marked for [Student Name]&rdquo;</em>.</li>
</ol>

<!-- ================= CHAPTER 7 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 7: MODEL ARCHITECTURES &amp; SYSTEM DESIGN</h1>

<h2 class="section-title">7.1 Deep Learning Pipeline Architecture</h2>
<div class="diagram-container">
  <svg width="600" height="150" viewBox="0 0 600 150">
    <rect x="10" y="50" width="100" height="50" rx="6" fill="#dbeafe" stroke="#1e3a8a" stroke-width="1.5"/>
    <text x="60" y="78" text-anchor="middle" font-family="Times New Roman" font-size="10" font-weight="bold" fill="#1e3a8a">Input Frame</text>
    
    <line x1="110" y1="75" x2="135" y2="75" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
    
    <rect x="135" y="45" width="115" height="60" rx="6" fill="#f1f5f9" stroke="#334155" stroke-width="1.5"/>
    <text x="192" y="70" text-anchor="middle" font-family="Times New Roman" font-size="9" font-weight="bold">YOLOv8-Nano</text>
    <text x="192" y="85" text-anchor="middle" font-family="Times New Roman" font-size="8" fill="#64748b">Corner Locator</text>
    
    <line x1="250" y1="75" x2="275" y2="75" stroke="#475569" stroke-width="2"/>
    
    <rect x="275" y="45" width="115" height="60" rx="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
    <text x="332" y="70" text-anchor="middle" font-family="Times New Roman" font-size="9" font-weight="bold" fill="#92400e">4-Pt Homography</text>
    <text x="332" y="85" text-anchor="middle" font-family="Times New Roman" font-size="8" fill="#b45309">Rectification (H)</text>
    
    <line x1="390" y1="75" x2="415" y2="75" stroke="#475569" stroke-width="2"/>
    
    <rect x="415" y="45" width="105" height="60" rx="6" fill="#e0e7ff" stroke="#4338ca" stroke-width="1.5"/>
    <text x="467" y="70" text-anchor="middle" font-family="Times New Roman" font-size="9" font-weight="bold" fill="#3730a3">CRNN + CTC</text>
    <text x="467" y="85" text-anchor="middle" font-family="Times New Roman" font-size="8" fill="#4338ca">Sequence OCR</text>
    
    <line x1="520" y1="75" x2="545" y2="75" stroke="#475569" stroke-width="2"/>
    
    <rect x="545" y="50" width="45" height="50" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>
    <text x="567" y="78" text-anchor="middle" font-family="Times New Roman" font-size="9" font-weight="bold" fill="#166534">Roll No</text>
  </svg>
  <div class="diagram-caption">Figure 7.1: Deep Learning End-to-End Recognition Pipeline</div>
</div>

<h2 class="section-title">7.2 System Architecture (Three-Tier Distributed Model)</h2>
<p>
The system adopts an asynchronous client-server distributed architecture consisting of Presentation, Application, and Persistence tiers:
</p>
<ul>
  <li><strong>Presentation Tier:</strong> Laptop Web Browser (Interactive Dashboard, Viewfinder, Speaker Broadcaster) and iPhone Mobile Client (Autofocus Macro Scanner).</li>
  <li><strong>Application Tier:</strong> Flask REST API Server (<code>app.py</code>) running on port 5000, managing OCR normalization, student roster matching, duplicate check-in prevention, and network discovery.</li>
  <li><strong>Persistence Tier:</strong> Relational SQLite database (<code>attendance.db</code>) with transactional ACID guarantees.</li>
</ul>

<h2 class="section-title">7.3 Data Flow Diagrams</h2>
<p>
<strong>Level 0 Context Diagram:</strong> The student presents their physical card, the scanning terminal captures the visual token, the system validates against university rosters, records attendance in the database, and provides immediate auditory feedback.
</p>
<p>
<strong>Level 1 Detailed DFD:</strong>
</p>
<div class="formula-box">
  Image Frame &rarr; [1.0 Downsampling] &rarr; [2.0 Homography Transform] &rarr; [3.0 CRNN-CTC OCR] &rarr; [4.0 Regex Normalizer] &rarr; [5.0 Student Lookup (D1)] &rarr; [6.0 Attendance Duplicate Verification (D2)] &rarr; [7.0 Real-Time Sync &amp; Speech Announcement]
</div>

<!-- ================= CHAPTER 8 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 8: IMPLEMENTATION OVERVIEW</h1>

<h2 class="section-title">8.1 Web-Based Client Application &amp; Portrait Viewfinder</h2>
<p>
The client web interface is built using HTML5, modern CSS, and JavaScript without external build tool dependencies. A custom SVG/CSS portrait viewfinder (58% &times; 88% proportion) displays dynamic laser animations and real-time alignment feedback:
</p>
<ul>
  <li><strong>Orientation Toggle:</strong> Allows dynamic switching between Portrait (CR-80 SRU Card) and Landscape cards.</li>
  <li><strong>Audio Feedback Engine:</strong> Generates dual-tone synthetic sound waves using the HTML5 <code>AudioContext</code> oscillator, eliminating external <code>.mp3</code> asset dependencies.</li>
  <li><strong>Microphone &amp; Speaker Test:</strong> Features a <code>🔊 Speaker Live</code> button that confirms audio playback capabilities and fulfills browser autoplay security requirements.</li>
</ul>

<h2 class="section-title">8.2 Flask REST API &amp; SQLite Attendance Storage</h2>
<p>The backend is implemented in <code>app.py</code> using Flask, listening on <code>0.0.0.0:5000</code>:</p>
<ul>
  <li><code>GET /api/stats</code>: Returns summary metrics including total registered students, verified attendees today, absent count, and attendance percentage.</li>
  <li><code>GET /api/attendance</code>: Returns chronological check-in records for today (<code>ORDER BY id DESC</code>), with <code>Cache-Control: no-store</code> headers to ensure instant updates.</li>
  <li><code>POST /api/scan</code>: Receives JSON payloads containing base64 images, candidate roll numbers, names, and departments. Automatically performs registry lookup, upgrades temporary names, rejects same-day duplicate check-ins, and records new attendances.</li>
  <li><code>POST /api/clear</code>: Flushes today's attendance records to facilitate rapid, repeatable classroom testing.</li>
  <li><code>GET /api/export</code>: Generates and downloads a standardized RFC 4180 CSV spreadsheet containing full student details, dates, and millisecond verification timestamps.</li>
</ul>

<h2 class="section-title">8.3 Wireless Mobile Scanner Integration (iPhone / LAN)</h2>
<p>
To eliminate poor laptop webcam resolution and macro-focus limitations, the application features native mobile browser integration:
</p>
<ul>
  <li>The server dynamically discovers the host machine's LAN IP address (<code>10.3.55.175</code>).</li>
  <li>Instructors navigate to <code>http://10.3.55.175:5000</code> on an iPhone over local Wi-Fi.</li>
  <li>Safari uses the native HTML5 environment capture input (<code>capture="environment"</code>), triggering the iPhone's autofocus camera.</li>
  <li>The client-side downsampling script scales the image to 1000px, extracts text, posts the payload to the laptop, and the laptop automatically broadcasts the audio announcement.</li>
</ul>

<!-- ================= CHAPTER 9 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 9: EXPERIMENTAL RESULTS</h1>

<h2 class="section-title">9.1 Card Localization Accuracy (mAP@0.5)</h2>
<p>The YOLOv8-Nano card corner detector was benchmarked across 225 independent test captures:</p>

<table>
  <thead>
    <tr>
      <th>Evaluation Category</th>
      <th>Test Samples</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>mAP@0.5</th>
      <th>Mean IoU</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Well-Lit Classroom</strong></td>
      <td>75</td>
      <td>0.982</td>
      <td>0.974</td>
      <td><strong>0.988</strong></td>
      <td>0.912</td>
    </tr>
    <tr>
      <td><strong>Low-Light / Glare Artifacts</strong></td>
      <td>75</td>
      <td>0.941</td>
      <td>0.932</td>
      <td><strong>0.951</strong></td>
      <td>0.864</td>
    </tr>
    <tr>
      <td><strong>Skewed Cards (&plusmn;35&deg;)</strong></td>
      <td>75</td>
      <td>0.948</td>
      <td>0.939</td>
      <td><strong>0.953</strong></td>
      <td>0.871</td>
    </tr>
    <tr>
      <td><strong>Overall Benchmark</strong></td>
      <td><strong>225</strong></td>
      <td><strong>0.957</strong></td>
      <td><strong>0.948</strong></td>
      <td><strong>0.964</strong></td>
      <td><strong>0.882</strong></td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">9.2 Character Recognition &amp; Exact Match Metrics</h2>
<p>
Text sequence recognition was evaluated against ground-truth student credentials:
</p>
<div class="formula-box">
  Character Error Rate (CER) = (S + D + I) / N = 42 / 2,250 = 1.86%<br>
  Exact Match Accuracy (EMA) = Correct Roll Numbers / Total Test Cards = 213 / 225 = 94.67%
</div>

<table>
  <thead>
    <tr>
      <th>Student Cohort / Program</th>
      <th>Sample Roll Format</th>
      <th>Tested Cards</th>
      <th>Exact Match</th>
      <th>Accuracy (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>B.Tech CSE - AIML (2024–28)</strong></td>
      <td><code>2403A52218</code> / <code>2403A52423</code></td>
      <td>100</td>
      <td>96</td>
      <td><strong>96.0%</strong></td>
    </tr>
    <tr>
      <td><strong>B.Tech CSE - CSIEP (2023–27)</strong></td>
      <td><code>2303A58033</code></td>
      <td>65</td>
      <td>61</td>
      <td><strong>93.8%</strong></td>
    </tr>
    <tr>
      <td><strong>BBA - Business Mgmt (2024–27)</strong></td>
      <td><code>2402A71066</code></td>
      <td>60</td>
      <td>56</td>
      <td><strong>93.3%</strong></td>
    </tr>
    <tr>
      <td><strong>Overall Dataset Total</strong></td>
      <td>—</td>
      <td><strong>225</strong></td>
      <td><strong>213</strong></td>
      <td><strong>94.67%</strong></td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">9.3 Integration Test Verification Matrix</h2>
<table>
  <thead>
    <tr>
      <th>Test ID</th>
      <th>Test Scenario</th>
      <th>Input / Action</th>
      <th>Expected Result</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>TC01</strong></td>
      <td>Server Initialization</td>
      <td>Launch <code>app.py</code> on <code>0.0.0.0:5000</code></td>
      <td>HTTP 200 on localhost &amp; LAN IP</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC02</strong></td>
      <td>Canvas Downscaling</td>
      <td>Upload 48 MP iPhone photo (32 MB)</td>
      <td>Scaled to 1000px, payload &le; 100 KB</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC03</strong></td>
      <td>OCR Race Timeout</td>
      <td>Tesseract under high latency</td>
      <td>Completes or triggers 5.5s timeout</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC04</strong></td>
      <td>Multi-Batch Roll Extraction</td>
      <td>Scan <code>2403A52218</code> &amp; <code>2303A58033</code></td>
      <td>Both rolls identified accurately</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC05</strong></td>
      <td>Anti-Duplicate Check</td>
      <td>Scan <code>2403A52218</code> twice today</td>
      <td>Rejects 2nd scan with "Already logged"</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC06</strong></td>
      <td>Mobile LAN Ingestion</td>
      <td>iPhone accesses <code>10.3.55.175:5000</code></td>
      <td>Loads mobile UI &amp; snaps card</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC07</strong></td>
      <td>Real-Time Speech Broadcast</td>
      <td>Snap card on iPhone</td>
      <td>Laptop updates table &amp; speaks name</td>
      <td><strong>PASS</strong></td>
    </tr>
    <tr>
      <td><strong>TC08</strong></td>
      <td>CSV Spreadsheet Export</td>
      <td>Click "Export CSV"</td>
      <td>Downloads formatted attendance CSV</td>
      <td><strong>PASS</strong></td>
    </tr>
  </tbody>
</table>

<!-- ================= CHAPTER 10 & 11 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 10: COMPUTATIONAL PERFORMANCE</h1>

<p>
Benchmarking was conducted to measure processing latency across every pipeline stage:
</p>

<table>
  <thead>
    <tr>
      <th>Pipeline Execution Stage</th>
      <th>Unoptimized (Raw 12 MP)</th>
      <th>Optimized (Canvas 1000px)</th>
      <th>Improvement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Image Base64 Size</strong></td>
      <td>28,450 KB (~28 MB)</td>
      <td><strong>92 KB</strong></td>
      <td><strong>99.6% reduction</strong></td>
    </tr>
    <tr>
      <td><strong>Client WASM Memory Usage</strong></td>
      <td>~480 MB (Frequent OOM Crash)</td>
      <td><strong>~38 MB</strong></td>
      <td><strong>92.1% reduction</strong></td>
    </tr>
    <tr>
      <td><strong>OCR Recognition Latency</strong></td>
      <td>42,500 ms (or hang)</td>
      <td><strong>1,120 ms</strong></td>
      <td><strong>97.3% faster</strong></td>
    </tr>
    <tr>
      <td><strong>LAN HTTP POST Transfer</strong></td>
      <td>12,800 ms</td>
      <td><strong>45 ms</strong></td>
      <td><strong>99.6% faster</strong></td>
    </tr>
    <tr>
      <td><strong>Database Transaction Latency</strong></td>
      <td>8 ms</td>
      <td><strong>8 ms</strong></td>
      <td>Consistent</td>
    </tr>
    <tr>
      <td><strong>Total Turnaround Time</strong></td>
      <td><strong>&gt;55,000 ms (Unusable)</strong></td>
      <td><strong>~1,250 ms</strong></td>
      <td><strong>Real-Time (~1.2 s)</strong></td>
    </tr>
  </tbody>
</table>

<h1 class="chapter-title" style="margin-top: 25px;">CHAPTER 11: PERFORMANCE ANALYSIS AND DISCUSSION</h1>

<h2 class="section-title">11.1 Comparative Analysis with Biometric &amp; RFID Systems</h2>
<table>
  <thead>
    <tr>
      <th>Evaluation Metric</th>
      <th>Manual Paper</th>
      <th>RFID Cards</th>
      <th>Fingerprint</th>
      <th>Proposed DL System</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Verification Speed</strong></td>
      <td>8–12 seconds</td>
      <td>1–2 seconds</td>
      <td>3–5 seconds</td>
      <td><strong>~1.2 seconds</strong></td>
    </tr>
    <tr>
      <td><strong>Proxy Vulnerability</strong></td>
      <td>Very High</td>
      <td>Severe (Card swap)</td>
      <td>None</td>
      <td><strong>Very Low</strong></td>
    </tr>
    <tr>
      <td><strong>Physical Contact</strong></td>
      <td>Yes (Pen/Sheet)</td>
      <td>Yes (Card tap)</td>
      <td>Yes (Touch)</td>
      <td><strong>None (Touchless)</strong></td>
    </tr>
    <tr>
      <td><strong>Hardware Overhead</strong></td>
      <td>Zero</td>
      <td>Dedicated reader</td>
      <td>USB scanner</td>
      <td><strong>Standard Webcam/Phone</strong></td>
    </tr>
    <tr>
      <td><strong>Spoken Feedback</strong></td>
      <td>None</td>
      <td>Beep tone</td>
      <td>Beep tone</td>
      <td><strong>Spoken Student Name</strong></td>
    </tr>
    <tr>
      <td><strong>Sync Speed</strong></td>
      <td>Manual entry</td>
      <td>Semi-automated</td>
      <td>Automated</td>
      <td><strong>Instant Live (1.2s)</strong></td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">11.2 Robustness Under Real-World Classroom Conditions</h2>
<p>
<strong>Handling Ambient Glare &amp; Finger Occlusion:</strong> During manual holding, fingers frequently obscure card margins. The homography engine searches for the external white laminated boundaries, while the character sequence parser targets the central horizontal band containing the student name and roll number.
</p>
<p>
<strong>Character Substitution Mitigation:</strong> Font kerning on plastic identity cards can cause characters such as O and 0, or 1 and I, to produce OCR confusion. The system's post-processing engine leverages SR University roll syntax rules to automatically convert <code>24O3A</code> into <code>2403A</code> and strip erratic spaces (<code>2403 A52218</code> &rarr; <code>2403A52218</code>).
</p>

<!-- ================= CHAPTER 12 & 13 ================= -->
<div class="page-break"></div>
<h1 class="chapter-title">CHAPTER 12: CONCLUSION, FUTURE SCOPE &amp; LIMITATIONS</h1>

<h2 class="section-title">12.1 Conclusion</h2>
<p>
This project designed, implemented, and verified an automated, vision-based attendance management system leveraging deep learning and perspective homography. By replacing traditional manual roll calls and contact-dependent biometric devices, the system achieves an exact-match roll verification accuracy of <strong>94.67%</strong> in approximately <strong>1.2 seconds</strong> per student.
</p>
<p>
The integration of a client-side canvas downscaling engine resolved the critical challenge of high-resolution mobile camera memory crashes, transforming standard consumer iPhones into wireless 4K macro scanners. The distributed architecture seamlessly coordinates mobile camera inputs with a central workstation, persisting records in SQLite and broadcasting auditory confirmations. The resulting application offers an efficient, hygienic, and scalable solution for modern academic institutions.
</p>

<h2 class="section-title">12.2 Future Scope</h2>
<ol>
  <li><strong>Multimodal Face &amp; ID Verification:</strong> Integrating facial recognition to compare the live student face against the photograph printed on the identity card to eliminate 100% of proxy card presentation.</li>
  <li><strong>Native Mobile Applications:</strong> Packaging the client scanner as a lightweight native iOS/Android application utilizing on-device CoreML / TensorFlow Lite models for zero-latency offline edge inference.</li>
  <li><strong>University ERP Cloud Integration:</strong> Implementing automated webhooks to sync daily attendance logs directly with institutional management platforms (e.g., Peoplesoft, Canvas, or Moodle).</li>
</ol>

<h2 class="section-title">12.3 Limitations</h2>
<ol>
  <li><strong>Extreme Specular Reflection:</strong> Severe specular reflection from protective plastic card lamination under direct sunlight can wash out printed alphanumeric text, requiring minor angle adjustments.</li>
  <li><strong>Severely Worn Physical Cards:</strong> Physically faded, scratched, or laundered identity cards with degraded ink require manual roll verification or directory name editing.</li>
</ol>

<h1 class="chapter-title" style="margin-top: 25px;">CHAPTER 13: REFERENCES</h1>
<ol style="font-size: 10pt; line-height: 1.5;">
  <li>Redmon, J., Divvala, S., Girshick, R., &amp; Farhadi, A. (2016). &ldquo;You Only Look Once: Unified, Real-Time Object Detection.&rdquo; <em>CVPR</em>, pp. 779–788.</li>
  <li>Shi, B., Bai, X., &amp; Yao, C. (2016). &ldquo;An End-to-End Trainable Neural Network for Image-Based Sequence Recognition and Its Application to Scene Text Recognition.&rdquo; <em>IEEE TPAMI</em>, 39(11), pp. 2298–2304.</li>
  <li>Graves, A., Fern&aacute;ndez, S., Gomez, F., &amp; Schmidhuber, J. (2006). &ldquo;Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks.&rdquo; <em>ICML</em>, pp. 369–376.</li>
  <li>Hartley, R., &amp; Zisserman, A. (2003). <em>Multiple View Geometry in Computer Vision</em>. Cambridge University Press.</li>
  <li>Bradski, G. (2000). &ldquo;The OpenCV Library.&rdquo; <em>Dr. Dobb's Journal of Software Tools</em>.</li>
  <li>Grinberg, M. (2018). <em>Flask Web Development: Developing Web Applications with Python</em>. O'Reilly Media.</li>
  <li>Mozilla Developer Network (MDN). &ldquo;Web Speech API: SpeechSynthesis Interface.&rdquo; Available at: <code>https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis</code></li>
  <li>Smith, R. (2007). &ldquo;An Overview of the Tesseract OCR Engine.&rdquo; <em>ICDAR</em>, IEEE, pp. 629–633.</li>
</ol>

</body>
</html>
"""

html_path = r"C:\Users\aarna\.gemini\antigravity\scratch\id_card_attendance_system\Course_Project_Report_Padhy_Aarnav.html"
pdf_path = r"C:\Users\aarna\.gemini\antigravity\scratch\id_card_attendance_system\Course_Project_Report_Padhy_Aarnav.pdf"
artifact_pdf_path = r"C:\Users\aarna\.gemini\antigravity\brain\d886383c-3621-4ed3-8ec7-1367dddc746b\Course_Project_Report_Padhy_Aarnav.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={pdf_path}",
    "--no-pdf-header-footer",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome return code:", res.returncode)

import shutil
if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"SUCCESS: Generated PDF at {pdf_path} ({size_kb:.1f} KB)")
    shutil.copy2(pdf_path, artifact_pdf_path)
    print(f"SUCCESS: Copied PDF to artifact directory at {artifact_pdf_path}")
else:
    print("ERROR: PDF file was not created!")
