"use client";

import { useState } from "react";
import api from "../services/api";
import PreviewTable from "./PreviewTable";
import ResultTable from "./ResultTable";

export default function UploadBox() {
    const [file, setFile] = useState<File | null>(null);
    const [preview, setPreview] = useState<any[]>([]);
    const [columns, setColumns] = useState<string[]>([]);
    const [uploadId, setUploadId] = useState<number | null>(null);
    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState<any>(null);

    // Upload CSV
    const uploadFile = async () => {

        if (!file) {
            alert("Please select a CSV file.");
            return;
        }

        setLoading(true);

        // Reset previous data
        setPreview([]);
        setColumns([]);
        setResult(null);
        setUploadId(null);

        try {

            const formData = new FormData();
            formData.append("file", file);

            const response = await api.post(
                "upload/",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            );

            setPreview(response.data.preview);
            setColumns(response.data.columns);
            setUploadId(response.data.upload_id);

        } catch (error: any) {

            console.log(error);

            alert(
                error.response?.data?.error ||
                "Upload Failed"
            );

        } finally {

            setLoading(false);

        }

    };

    // Import CSV
    const importCSV = async () => {

        if (!uploadId) return;

        setLoading(true);

        try {

            const response = await api.post("import/", {
                upload_id: uploadId,
            });

            setResult(response.data);

        } catch (error: any) {

            console.log(error);

            alert(
                error.response?.data?.error ||
                "Import Failed"
            );

        } finally {

            setLoading(false);

        }

    };

    return (

        <div className="max-w-7xl mx-auto p-8">

            <h1 className="text-4xl font-bold mb-6 text-center">
                AI Powered CSV Importer
            </h1>

            <div className="border rounded-lg p-6 shadow">

                <input
                    type="file"
                    accept=".csv"
                    onChange={(e) => {

                        if (e.target.files) {

                            setFile(e.target.files[0]);

                        }

                    }}
                />

                {file && (

                    <p className="mt-2 text-sm">
                        Selected File:
                        <strong> {file.name}</strong>
                    </p>

                )}

                <button
                    className="mt-5 bg-blue-600 text-white px-6 py-2 rounded disabled:bg-gray-400"
                    onClick={uploadFile}
                    disabled={loading}
                >
                    Upload CSV
                </button>

            </div>

            {loading && (

                <div className="mt-6 text-blue-600 font-semibold text-lg">
                    Processing...
                </div>

            )}

            <PreviewTable
                columns={columns}
                preview={preview}
            />

            {uploadId && !loading && (

                <button
                    onClick={importCSV}
                    className="mt-6 bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700"
                >
                    Confirm Import
                </button>

            )}

            {result && (

                <>
                    <div className="mt-8 border rounded-lg p-5 shadow">

                        <h2 className="text-2xl font-bold mb-4">
                            Import Summary
                        </h2>

                        <p>
                            <strong>Total Rows:</strong> {result.total_rows}
                        </p>

                        <p>
                            <strong>Imported:</strong> {result.imported}
                        </p>

                        <p>
                            <strong>Skipped:</strong> {result.skipped}
                        </p>

                    </div>

                    <ResultTable
                        records={result.records}
                    />
                </>

            )}

        </div>

    );
}