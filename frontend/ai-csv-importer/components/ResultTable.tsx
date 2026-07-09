"use client";

interface Props {
    records: any[];
}

export default function ResultTable({ records }: Props) {

    if (!records || records.length === 0) {
        return null;
    }

    return (

        <div className="mt-8 overflow-x-auto border rounded-lg">

            <h2 className="text-2xl font-bold mb-4 p-4">
                Imported CRM Records
            </h2>

            <table className="min-w-full border-collapse">

                <thead className="bg-gray-200">

                    <tr>
                        <th className="border px-4 py-2">Name</th>
                        <th className="border px-4 py-2">Email</th>
                        <th className="border px-4 py-2">Mobile</th>
                        <th className="border px-4 py-2">Company</th>
                        <th className="border px-4 py-2">City</th>
                        <th className="border px-4 py-2">Status</th>
                    </tr>

                </thead>

                <tbody>

                    {records.map((lead: any) => (

                        <tr key={lead.id}>

                            <td className="border px-4 py-2">{lead.name}</td>
                            <td className="border px-4 py-2">{lead.email}</td>
                            <td className="border px-4 py-2">
                                {lead.mobile_without_country_code}
                            </td>
                            <td className="border px-4 py-2">{lead.company}</td>
                            <td className="border px-4 py-2">{lead.city}</td>
                            <td className="border px-4 py-2">
                                {lead.crm_status}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}