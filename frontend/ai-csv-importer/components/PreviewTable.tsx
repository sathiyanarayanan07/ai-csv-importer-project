"use client";

interface Props {
    columns: string[];
    preview: any[];
}

export default function PreviewTable({ columns, preview }: Props) {

    if (preview.length === 0) {
        return null;
    }

    return (

        <div className="mt-8 overflow-x-auto border rounded-lg">

            <h2 className="text-2xl font-bold mb-4">
                CSV Preview
            </h2>

            <table className="min-w-full border">

                <thead className="bg-gray-200">

                    <tr>

                        {columns.map((column) => (

                            <th
                                key={column}
                                className="border px-4 py-2"
                            >
                                {column}
                            </th>

                        ))}

                    </tr>

                </thead>

                <tbody>

                    {preview.map((row, index) => (

                        <tr key={index}>

                            {columns.map((column) => (

                                <td
                                    key={column}
                                    className="border px-4 py-2"
                                >
                                    {row[column]}
                                </td>

                            ))}

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}