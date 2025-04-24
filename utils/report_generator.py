import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df, actuals, predictions, filename):
    # Prepare data for the report
    report_data = []
    report_data.append(["Timestamp", "Actual (MW)", "Predicted (MW)"])
    
    for i in range(len(actuals)):
        timestamp = df['Datetime'].iloc[i]
        actual = f"{actuals[i][0]:.2f}"
        predicted = f"{predictions[i][0]:.2f}"
        report_data.append([str(timestamp), actual, predicted])
    
    # Limit to first 100 rows for the report
    report_data = report_data[:101]  # Header + 100 rows
    
    # Create PDF
    report_path = os.path.join("reports", f"report_{filename.split('.')[0]}.pdf")
    doc = SimpleDocTemplate(report_path, pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    elements.append(Paragraph("Energy Usage Prediction Report", styles['Title']))
    elements.append(Paragraph(f"Generated for file: {filename}", styles['Normal']))
    elements.append(Paragraph("<br/><br/>", styles['Normal']))
    
    # Create table
    table = Table(report_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    
    return report_path