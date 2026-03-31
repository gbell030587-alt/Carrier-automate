from flask import Flask, request, send_file, jsonify
import os
import subprocess

app = Flask(__name__)

WORKDIR = tmpcarrier_job
os.makedirs(WORKDIR, exist_ok=True)

@app.route(run, methods=[POST])
def run_job():
    try
        kpi = request.files.get(kpi_file)
        sla = request.files.get(sla_file)
        rate = request.files.get(rate_file)
        script = request.files.get(script_file)

        if not kpi or not sla or not rate or not script
            return jsonify({
                error Missing one or more required files kpi_file, sla_file, rate_file, script_file
            }), 400

        kpi_path = os.path.join(WORKDIR, KPI RAW TEST.xlsx)
        sla_path = os.path.join(WORKDIR, Simple_SLA_Submission_Template.xlsx)
        rate_path = os.path.join(WORKDIR, Carrier_RateEngine_Templates.xlsx)
        script_path = os.path.join(WORKDIR, Python script.txt)

        kpi.save(kpi_path)
        sla.save(sla_path)
        rate.save(rate_path)
        script.save(script_path)

        # patch the script so pandas reads the first sheet instead of all sheets
        with open(script_path, r, encoding=utf-8) as f
            code = f.read()

        code = code.replace(RAW_KPI_SHEET = None, RAW_KPI_SHEET = 0, 1)

        patched_script_path = os.path.join(WORKDIR, Python_script_fixed.py)
        with open(patched_script_path, w, encoding=utf-8) as f
            f.write(code)

        result = subprocess.run(
            [python, patched_script_path],
            cwd=WORKDIR,
            capture_output=True,
            text=True
        )

        if result.returncode != 0
            return jsonify({
                error Script failed,
                stdout result.stdout,
                stderr result.stderr
            }), 500

        output_path = os.path.join(WORKDIR, KPI_RAW_TEST_populated_SLA_and_Cost.xlsx)

        if not os.path.exists(output_path)
            return jsonify({
                error Output file not found,
                stdout result.stdout,
                stderr result.stderr
            }), 500

        return send_file(
            output_path,
            as_attachment=True,
            download_name=KPI_RAW_TEST_populated_SLA_and_Cost.xlsx,
            mimetype=applicationvnd.openxmlformats-officedocument.spreadsheetml.sheet
        )

    except Exception as e
        return jsonify({error str(e)}), 500


@app.route(, methods=[GET])
def health()
    return jsonify({status ok})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
