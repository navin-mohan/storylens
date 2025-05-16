"use client"

import type React from "react"

import { useState } from "react"
import Link from "next/link"
import { Search, PlusCircle } from "lucide-react"
import { useRouter } from "next/navigation"
import AddStoryModal from "./add-story-modal"


export function Navbar() {
  const [searchQuery, setSearchQuery] = useState("")
  const [isModalOpen, setIsModalOpen] = useState(false)
  const router = useRouter()

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (searchQuery.trim()) {
      router.push(`/search?q=${encodeURIComponent(searchQuery.trim())}`)
    }
  }

  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <Link href="/" className="text-xl font-bold">
            StoryLens
          </Link>

          <div className="flex items-center space-x-4">
            <form onSubmit={handleSearch} className="relative">
              <input
                type="text"
                placeholder="Search stories..."
                className="w-64 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              <button type="submit" className="absolute right-2 top-1/2 transform -translate-y-1/2 text-gray-500">
                <Search size={18} />
              </button>
            </form>

            <button
              onClick={() => setIsModalOpen(true)}
              className="flex items-center space-x-1 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors"
            >
              <PlusCircle size={18} />
              <span>Add Story</span>
            </button>
          </div>
        </div>
      </div>

      <AddStoryModal isOpen={isModalOpen} onClose={() => {
        setIsModalOpen(false)
      }} />
    </nav>
  )
}
